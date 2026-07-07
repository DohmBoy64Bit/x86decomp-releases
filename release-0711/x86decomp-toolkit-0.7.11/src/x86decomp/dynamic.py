"""Bounded differential execution using Unicorn.

This validator is intentionally explicit about its execution envelope. It can
compare leaf routines and routines whose external calls are represented by
user-supplied deterministic stubs. It does not model a complete Windows process.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .util import load_json, sha256_bytes, utc_now, write_json

PAGE_SIZE = 0x1000


def _unicorn() -> tuple[Any, Any, Any]:
    """Import the optional Unicorn engine and x86 constants.

    Returns:
        A ``(unicorn, x86_const, Uc)`` tuple of the module, its ``x86_const`` submodule,
        and the ``Uc`` engine class.

    Raises:
        ExternalToolError: If Unicorn is not installed.
    """
    try:
        import unicorn  # type: ignore
        from unicorn import x86_const  # type: ignore
    except ImportError as exc:
        raise ExternalToolError(
            "Unicorn is required for differential execution; install x86decomp-toolkit[dynamic]"
        ) from exc
    return unicorn, x86_const, unicorn.Uc


def _align_down(value: int) -> int:
    """Round ``value`` down to the start of its containing page.

    Args:
        value: Address to align.

    Returns:
        ``value`` rounded down to a ``PAGE_SIZE`` boundary.
    """
    return value & ~(PAGE_SIZE - 1)


def _align_up(value: int) -> int:
    """Round ``value`` up to the next page boundary.

    Args:
        value: Address to align.

    Returns:
        ``value`` rounded up to a ``PAGE_SIZE`` boundary.
    """
    return (value + PAGE_SIZE - 1) & ~(PAGE_SIZE - 1)


@dataclass(frozen=True)
class MemoryRegion:
    """Immutable description of a mapped memory region.

    Holds the region ``address``, its initial ``data`` bytes, and the total mapped ``size``
    (which is at least ``len(data)``).
    """
    address: int
    data: bytes
    size: int


@dataclass(frozen=True)
class ExecutionSpec:
    """Immutable, validated harness describing a bounded Unicorn execution.

    Captures the architecture, code/stack/sentinel base addresses, instruction and time
    limits, initial register values, stack argument bytes, preloaded memory regions, the
    registers and memory ranges to observe, and deterministic call stubs keyed by address.
    """
    architecture: str
    code_base: int
    stack_base: int
    stack_size: int
    sentinel_address: int
    max_instructions: int
    timeout_ms: int
    registers: dict[str, int]
    stack_arguments: bytes
    memory: tuple[MemoryRegion, ...]
    observe_registers: tuple[str, ...]
    observe_memory: tuple[tuple[int, int], ...]
    stubs: dict[int, dict[str, int]]


def load_execution_spec(path: Path) -> ExecutionSpec:
    """Load and validate a differential execution harness from JSON.

    Parses architecture, address bases, limits, initial registers, stack arguments, memory
    regions, observation lists, and call stubs into an :class:`ExecutionSpec`.

    Args:
        path: Path to the harness JSON document.

    Returns:
        The validated :class:`ExecutionSpec`.

    Raises:
        ContractError: If the harness is not an object, the architecture is unsupported, a
            numeric field is not a positive integer, registers/stubs are not string-to-int
            objects, hex fields are malformed, a memory size does not cover its data, or an
            observation entry is invalid.
    """
    value = load_json(path)
    if not isinstance(value, dict):
        raise ContractError("execution harness must be an object")
    architecture = value.get("architecture", "x86")
    if architecture not in ("x86", "x86_64"):
        raise ContractError("execution architecture must be x86 or x86_64")
    defaults = {
        "code_base": 0x1000000,
        "stack_base": 0x70000000 if architecture == "x86" else 0x700000000000,
        "stack_size": 0x20000,
        "sentinel_address": 0x0FFF0000 if architecture == "x86" else 0x00000000FFF00000,
        "max_instructions": 100000,
        "timeout_ms": 1000,
    }
    integers: dict[str, int] = {}
    for key, default in defaults.items():
        raw = value.get(key, default)
        if not isinstance(raw, int) or isinstance(raw, bool) or raw <= 0:
            raise ContractError(f"{key} must be a positive integer")
        integers[key] = raw
    registers_raw = value.get("registers", {})
    if not isinstance(registers_raw, dict) or not all(
        isinstance(k, str) and isinstance(v, int) for k, v in registers_raw.items()
    ):
        raise ContractError("registers must be a string-to-integer object")
    stack_arguments_hex = value.get("stack_arguments_hex", "")
    if not isinstance(stack_arguments_hex, str):
        raise ContractError("stack_arguments_hex must be a string")
    try:
        stack_arguments = bytes.fromhex(stack_arguments_hex)
    except ValueError as exc:
        raise ContractError("stack_arguments_hex is invalid hex") from exc
    memory_records: list[MemoryRegion] = []
    for index, item in enumerate(value.get("memory", [])):
        if not isinstance(item, dict):
            raise ContractError(f"memory[{index}] must be an object")
        address = item.get("address")
        data_hex = item.get("data_hex", "")
        size = item.get("size")
        if not isinstance(address, int) or address < 0 or not isinstance(data_hex, str):
            raise ContractError(f"memory[{index}] has invalid address or data_hex")
        try:
            data = bytes.fromhex(data_hex)
        except ValueError as exc:
            raise ContractError(f"memory[{index}].data_hex is invalid") from exc
        if size is None:
            size = len(data)
        if not isinstance(size, int) or size < len(data) or size <= 0:
            raise ContractError(f"memory[{index}].size must cover data and be positive")
        memory_records.append(MemoryRegion(address=address, data=data, size=size))
    observe_registers = value.get("observe_registers", ["eax", "ecx", "edx", "esp", "eflags"] if architecture == "x86" else ["rax", "rcx", "rdx", "rsp", "rflags"])
    if not isinstance(observe_registers, list) or not all(isinstance(item, str) for item in observe_registers):
        raise ContractError("observe_registers must be an array of strings")
    observe_memory: list[tuple[int, int]] = []
    for index, item in enumerate(value.get("observe_memory", [])):
        if not isinstance(item, dict) or not isinstance(item.get("address"), int) or not isinstance(item.get("size"), int):
            raise ContractError(f"observe_memory[{index}] must contain integer address and size")
        if item["size"] <= 0:
            raise ContractError("observe_memory size must be positive")
        observe_memory.append((item["address"], item["size"]))
    stubs: dict[int, dict[str, int]] = {}
    for key, stub in value.get("stubs", {}).items():
        try:
            address = int(key, 0)
        except (ValueError, TypeError) as exc:
            raise ContractError(f"stub address is invalid: {key}") from exc
        if not isinstance(stub, dict) or not all(isinstance(k, str) and isinstance(v, int) for k, v in stub.items()):
            raise ContractError(f"stub {key} must be a string-to-integer object")
        stubs[address] = dict(stub)
    return ExecutionSpec(
        architecture=architecture,
        code_base=integers["code_base"],
        stack_base=integers["stack_base"],
        stack_size=integers["stack_size"],
        sentinel_address=integers["sentinel_address"],
        max_instructions=integers["max_instructions"],
        timeout_ms=integers["timeout_ms"],
        registers=dict(registers_raw),
        stack_arguments=stack_arguments,
        memory=tuple(memory_records),
        observe_registers=tuple(item.lower() for item in observe_registers),
        observe_memory=tuple(observe_memory),
        stubs=stubs,
    )


def _register_map(architecture: str, x86_const: Any) -> dict[str, int]:
    """Build a mapping from register name to its Unicorn x86 register constant.

    Args:
        architecture: ``"x86"`` or ``"x86_64"``; 64-bit names are included only for x86_64.
        x86_const: Unicorn ``x86_const`` module supplying the register constants.

    Returns:
        A mapping of lowercase register name to Unicorn register constant for registers the
        installed Unicorn build exposes.
    """
    names32 = [
        "eax", "ebx", "ecx", "edx", "esi", "edi", "ebp", "esp", "eip", "eflags",
        "ax", "bx", "cx", "dx", "al", "ah", "bl", "bh", "cl", "ch", "dl", "dh",
    ]
    names64 = [
        "rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "rip", "rflags",
        "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
    ]
    result: dict[str, int] = {}
    for name in names32 + (names64 if architecture == "x86_64" else []):
        constant = getattr(x86_const, f"UC_X86_REG_{name.upper()}", None)
        if constant is not None:
            result[name] = constant
    return result


def _map_region(uc: Any, mapped: list[tuple[int, int]], address: int, size: int, permissions: int) -> None:
    """Map a page-aligned memory region into the emulator, tolerating full containment.

    Args:
        uc: Unicorn engine instance.
        mapped: List of already-mapped ``(start, end)`` ranges; appended to on success.
        address: Base address of the region to map.
        size: Size of the region in bytes.
        permissions: Unicorn protection flags for the mapping.

    Raises:
        ContractError: If the aligned range partially overlaps an existing mapping.
    """
    start = _align_down(address)
    end = _align_up(address + size)
    for existing_start, existing_end in mapped:
        if start < existing_end and existing_start < end:
            if existing_start <= start and end <= existing_end:
                return
            raise ContractError(f"overlapping Unicorn mappings: 0x{start:x}-0x{end:x}")
    uc.mem_map(start, end - start, permissions)
    mapped.append((start, end))


def execute_code(code: bytes, spec: ExecutionSpec, *, code_base: int | None = None) -> dict[str, Any]:
    """Emulate a code blob under a harness and capture observed registers and memory.

    Maps code, stack, sentinel, harness memory, and stub pages; seeds registers and the
    stack; installs a code hook that enforces the instruction/time limits, handles the
    return sentinel, and applies deterministic call stubs; then runs to completion.

    Args:
        code: Machine code blob to execute.
        spec: Validated execution harness.
        code_base: Optional override for the code load address; defaults to ``spec.code_base``.

    Returns:
        A result dictionary with the code hash and base, stop reason, any Unicorn error,
        instruction count, observed register values, observed memory, and whether the
        routine returned to the sentinel.

    Raises:
        ContractError: If ``code`` is empty, an initial register is unsupported, an observed
            register is unsupported, or region mapping fails.
    """
    unicorn, x86_const, Uc = _unicorn()
    if not code:
        raise ContractError("code may not be empty")
    mode = unicorn.UC_MODE_32 if spec.architecture == "x86" else unicorn.UC_MODE_64
    uc = Uc(unicorn.UC_ARCH_X86, mode)
    registers = _register_map(spec.architecture, x86_const)
    actual_code_base = spec.code_base if code_base is None else code_base
    pointer_size = 4 if spec.architecture == "x86" else 8
    pc_name = "eip" if spec.architecture == "x86" else "rip"
    sp_name = "esp" if spec.architecture == "x86" else "rsp"
    return_name = "eax" if spec.architecture == "x86" else "rax"
    mapped: list[tuple[int, int]] = []
    _map_region(uc, mapped, actual_code_base, len(code), unicorn.UC_PROT_ALL)
    uc.mem_write(actual_code_base, code)
    _map_region(uc, mapped, spec.stack_base, spec.stack_size, unicorn.UC_PROT_ALL)
    _map_region(uc, mapped, spec.sentinel_address, 1, unicorn.UC_PROT_ALL)
    uc.mem_write(spec.sentinel_address, b"\xcc")
    for region in spec.memory:
        _map_region(uc, mapped, region.address, region.size, unicorn.UC_PROT_ALL)
        if region.data:
            uc.mem_write(region.address, region.data)
    for stub_address in spec.stubs:
        _map_region(uc, mapped, stub_address, 1, unicorn.UC_PROT_ALL)
        uc.mem_write(stub_address, b"\xcc")

    stack_pointer = spec.stack_base + spec.stack_size - 0x100
    stack_pointer &= ~(pointer_size - 1)
    uc.mem_write(stack_pointer, spec.sentinel_address.to_bytes(pointer_size, "little"))
    if spec.stack_arguments:
        uc.mem_write(stack_pointer + pointer_size, spec.stack_arguments)
    uc.reg_write(registers[sp_name], stack_pointer)
    for name, value in spec.registers.items():
        normalized = name.lower()
        if normalized not in registers:
            raise ContractError(f"unsupported initial register: {name}")
        uc.reg_write(registers[normalized], value)
    uc.reg_write(registers[pc_name], actual_code_base)

    instruction_count = 0
    stop_reason = "unknown"
    start_time = time.monotonic()

    def code_hook(uc_obj: Any, address: int, size: int, _user_data: Any) -> None:
        """Per-instruction Unicorn hook enforcing limits, the sentinel, and call stubs.

        Counts instructions, stops at the return sentinel, applies any stub at ``address``
        (setting the return value, popping the return address, and adjusting the stack), and
        stops on the instruction or time limit.

        Args:
            uc_obj: The Unicorn engine instance invoking the hook.
            address: Address of the instruction about to execute.
            size: Size of the instruction in bytes.
            _user_data: Unused Unicorn user-data argument.
        """
        nonlocal instruction_count, stop_reason
        instruction_count += 1
        if address == spec.sentinel_address:
            stop_reason = "returned"
            uc_obj.emu_stop()
            return
        stub = spec.stubs.get(address)
        if stub is not None:
            if "return_value" in stub:
                uc_obj.reg_write(registers[return_name], stub["return_value"])
            current_sp = uc_obj.reg_read(registers[sp_name])
            return_address = int.from_bytes(uc_obj.mem_read(current_sp, pointer_size), "little")
            stack_pop = stub.get("stack_pop", 0)
            uc_obj.reg_write(registers[sp_name], current_sp + pointer_size + stack_pop)
            uc_obj.reg_write(registers[pc_name], return_address)
        if instruction_count >= spec.max_instructions:
            stop_reason = "instruction_limit"
            uc_obj.emu_stop()
        if (time.monotonic() - start_time) * 1000 >= spec.timeout_ms:
            stop_reason = "timeout"
            uc_obj.emu_stop()

    uc.hook_add(unicorn.UC_HOOK_CODE, code_hook)
    error: str | None = None
    try:
        uc.emu_start(actual_code_base, 0, timeout=spec.timeout_ms * 1000, count=spec.max_instructions)
        if stop_reason == "unknown":
            stop_reason = "emulator_stopped"
    except unicorn.UcError as exc:
        stop_reason = "unicorn_error"
        error = str(exc)

    register_output: dict[str, int] = {}
    for name in spec.observe_registers:
        if name not in registers:
            raise ContractError(f"unsupported observed register: {name}")
        register_output[name] = int(uc.reg_read(registers[name]))
    memory_output: list[dict[str, Any]] = []
    for address, size in spec.observe_memory:
        try:
            data = bytes(uc.mem_read(address, size))
            memory_output.append({"address": address, "size": size, "data_hex": data.hex()})
        except unicorn.UcError as exc:
            memory_output.append({"address": address, "size": size, "error": str(exc)})
    return {
        "code_sha256": sha256_bytes(code),
        "code_base": actual_code_base,
        "stop_reason": stop_reason,
        "error": error,
        "instruction_count": instruction_count,
        "registers": register_output,
        "memory": memory_output,
        "completed_return": stop_reason == "returned",
    }


def differential_validate(
    target: bytes,
    candidate: bytes,
    spec: ExecutionSpec,
    *,
    target_base: int | None = None,
    candidate_base: int | None = None,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Run target and candidate under one harness and diff their observable behavior.

    Compares observed registers (ignoring the program counter), observed memory ranges, and
    termination status to decide harness-scoped equivalence.

    Args:
        target: Reference code blob.
        candidate: Candidate code blob.
        spec: Shared execution harness.
        target_base: Optional code load address for the target.
        candidate_base: Optional code load address for the candidate.
        report_path: Optional path to write the JSON report.

    Returns:
        A report with both execution results, the list of differences, and the
        harness-scoped equivalence verdict.
    """
    target_result = execute_code(target, spec, code_base=target_base)
    candidate_result = execute_code(candidate, spec, code_base=candidate_base)
    differences: list[dict[str, Any]] = []
    for register in spec.observe_registers:
        left = target_result["registers"].get(register)
        right = candidate_result["registers"].get(register)
        # Stack/program counters depend on code mapping. Compare stack deltas separately.
        if register in ("eip", "rip"):
            continue
        if left != right:
            differences.append({"kind": "register", "name": register, "target": left, "candidate": right})
    target_memory = {(item["address"], item["size"]): item for item in target_result["memory"]}
    candidate_memory = {(item["address"], item["size"]): item for item in candidate_result["memory"]}
    for key in sorted(set(target_memory) | set(candidate_memory)):
        if target_memory.get(key) != candidate_memory.get(key):
            differences.append(
                {"kind": "memory", "address": key[0], "size": key[1], "target": target_memory.get(key), "candidate": candidate_memory.get(key)}
            )
    if target_result["completed_return"] != candidate_result["completed_return"]:
        differences.append(
            {"kind": "termination", "target": target_result["stop_reason"], "candidate": candidate_result["stop_reason"]}
        )
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "bounded_unicorn_differential",
        "architecture": spec.architecture,
        "equivalent_for_harness": not differences and target_result["completed_return"] and candidate_result["completed_return"],
        "target": target_result,
        "candidate": candidate_result,
        "differences": differences,
        "semantic_equivalence_claimed": False,
        "scope_statement": "Result applies only to the supplied initial state, deterministic stubs, observed registers, observed memory, and execution bounds.",
    }
    if report_path is not None:
        write_json(report_path, report)
    return report


def differential_validate_files(
    target_path: Path,
    candidate_path: Path,
    harness_path: Path,
    *,
    target_base: int | None = None,
    candidate_base: int | None = None,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Read code blobs and a harness from files and run :func:`differential_validate`.

    Args:
        target_path: Path to the reference code blob.
        candidate_path: Path to the candidate code blob.
        harness_path: Path to the execution harness JSON.
        target_base: Optional code load address for the target.
        candidate_base: Optional code load address for the candidate.
        report_path: Optional path to write the JSON report.

    Returns:
        The differential validation report.

    Raises:
        ContractError: If either code file does not exist.
    """
    if not target_path.is_file() or not candidate_path.is_file():
        raise ContractError("target and candidate code files must exist")
    return differential_validate(
        target_path.read_bytes(),
        candidate_path.read_bytes(),
        load_execution_spec(harness_path),
        target_base=target_base,
        candidate_base=candidate_base,
        report_path=report_path,
    )

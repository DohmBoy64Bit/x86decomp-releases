"""Generate bounded differential-execution harnesses from explicit ABI facts.

Generated values are deterministic test inputs, not recovered original inputs.
Pointer regions are allocated only when the user declares pointer parameters.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .abi import ABIContract, load_abi_contract
from .errors import ContractError
from .util import load_json, utc_now, write_json


def _deterministic_word(index: int, bits: int) -> int:
    """Generate a reproducible fixed-width integer for a corpus case index."""
    mask = (1 << bits) - 1
    return (0x13579BDF2468ACE0 + index * 0x102030405060708) & mask


def generate_execution_harness(
    abi_contract: ABIContract,
    *,
    output: Path | None = None,
    pointer_parameters: list[dict[str, Any]] | None = None,
    observe_pointer_parameters: bool = True,
    max_instructions: int = 100000,
    timeout_ms: int = 1000,
) -> dict[str, Any]:
    """Generate execution harness."""
    if max_instructions <= 0 or timeout_ms <= 0:
        raise ContractError("harness bounds must be positive")
    architecture = abi_contract.architecture
    pointer_size = 4 if architecture == "x86" else 8
    pointer_bits = pointer_size * 8
    code_base = 0x01000000 if architecture == "x86" else 0x0000000100000000
    stack_base = 0x70000000 if architecture == "x86" else 0x0000700000000000
    memory_base = 0x20000000 if architecture == "x86" else 0x0000000200000000
    sentinel = 0x0FFF0000 if architecture == "x86" else 0x00000000FFF00000
    registers: dict[str, int] = {}
    stack_words: list[int] = []
    memory: list[dict[str, Any]] = []
    observe_memory: list[dict[str, Any]] = []
    pointer_specs = pointer_parameters or []
    by_position: dict[int, dict[str, Any]] = {}
    for item in pointer_specs:
        if not isinstance(item, dict) or not isinstance(item.get("position"), int):
            raise ContractError("pointer parameter records require integer position")
        position = item["position"]
        if position < 0 or position in by_position:
            raise ContractError("pointer parameter positions must be unique non-negative integers")
        size = item.get("size", 64)
        if not isinstance(size, int) or size <= 0 or size > 1024 * 1024:
            raise ContractError("pointer parameter size must be 1..1048576")
        by_position[position] = item
    register_order = list(abi_contract.register_arguments)
    argument_count = max(
        len(register_order) + ((abi_contract.stack_argument_bytes or 0) // pointer_size),
        max(by_position.keys(), default=-1) + 1,
    )
    argument_values: list[int] = []
    for index in range(argument_count):
        pointer = by_position.get(index)
        if pointer is None:
            value = _deterministic_word(index, pointer_bits)
        else:
            address = memory_base + index * 0x10000
            data_hex = pointer.get("data_hex")
            if data_hex is None:
                data = bytes(((index + offset) * 17 + 3) & 0xFF for offset in range(pointer.get("size", 64)))
            elif isinstance(data_hex, str):
                try:
                    data = bytes.fromhex(data_hex)
                except ValueError as exc:
                    raise ContractError("pointer parameter data_hex is invalid") from exc
            else:
                raise ContractError("pointer parameter data_hex must be a string")
            size = int(pointer.get("size", max(len(data), 1)))
            if len(data) > size:
                raise ContractError("pointer parameter data exceeds declared size")
            memory.append({"address": address, "size": size, "data_hex": data.hex()})
            if observe_pointer_parameters:
                observe_memory.append({"address": address, "size": size})
            value = address
        argument_values.append(value)
    for index, register in enumerate(register_order):
        if index < len(argument_values):
            registers[register] = argument_values[index]
    stack_values = argument_values[len(register_order) :]
    for value in stack_values:
        stack_words.append(value)
    stack_arguments = b"".join(value.to_bytes(pointer_size, "little") for value in stack_words)
    if abi_contract.this_register and abi_contract.this_register not in registers:
        # A declared this pointer receives its own object region.
        address = memory_base + 0x01000000
        registers[abi_contract.this_register] = address
        memory.append({"address": address, "size": 256, "data_hex": bytes(range(256)).hex()})
        if observe_pointer_parameters:
            observe_memory.append({"address": address, "size": 256})
    observe_registers = list(dict.fromkeys([
        *abi_contract.return_registers,
        "esp" if architecture == "x86" else "rsp",
        "eflags" if architecture == "x86" else "rflags",
    ]))
    harness = {
        "schema_version": 1,
        "created_at": utc_now(),
        "architecture": architecture,
        "code_base": code_base,
        "stack_base": stack_base,
        "stack_size": 0x20000,
        "sentinel_address": sentinel,
        "max_instructions": max_instructions,
        "timeout_ms": timeout_ms,
        "registers": registers,
        "stack_arguments_hex": stack_arguments.hex(),
        "memory": memory,
        "observe_registers": observe_registers,
        "observe_memory": observe_memory,
        "stubs": {},
        "generation": {
            "source": "explicit_abi_contract",
            "deterministic_test_values": True,
            "original_runtime_inputs_claimed": False,
            "external_calls_modeled": False,
            "calling_convention": abi_contract.convention.value,
        },
        "limitations": [
            "Generated values are deterministic test inputs and are not recovered production inputs.",
            "External calls require explicit deterministic stubs before execution.",
            "Passing this harness demonstrates equality only inside its declared observations and bounds.",
        ],
    }
    if output is not None:
        write_json(output, harness)
    return harness


def generate_execution_harness_from_files(
    abi_contract_path: Path,
    output: Path,
    *,
    pointer_parameters_path: Path | None = None,
    observe_pointer_parameters: bool = True,
    max_instructions: int = 100000,
    timeout_ms: int = 1000,
) -> dict[str, Any]:
    """Generate execution harness from files."""
    pointers: list[dict[str, Any]] | None = None
    if pointer_parameters_path is not None:
        raw = load_json(pointer_parameters_path)
        if not isinstance(raw, list):
            raise ContractError("pointer parameter file must contain an array")
        pointers = raw
    return generate_execution_harness(
        load_abi_contract(abi_contract_path),
        output=output,
        pointer_parameters=pointers,
        observe_pointer_parameters=observe_pointer_parameters,
        max_instructions=max_instructions,
        timeout_ms=timeout_ms,
    )

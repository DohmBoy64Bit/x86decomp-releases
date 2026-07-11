"""Materialize assembly source, relocations, and COFF objects."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from x86decomp.contracts import ContractError, atomic_write_bytes, sha256_bytes, sha256_file

from .annotation import byte_directive_lines, render_byte_assembly, validate_symbol
from .relocations import RelocationResolver, SymbolAddress, normalize_symbol_map

_SAFE_SYMBOL_RE = re.compile(r"^[A-Za-z_.$?@][A-Za-z0-9_.$?@-]*$")


class AssemblerError(ContractError):
    """Assembler failure with source line numbers retained for focused fallback."""

    def __init__(self, message: str, *, line_numbers: Sequence[int] = ()) -> None:
        """Initialize AssemblerError with `message`, `line_numbers`."""
        super().__init__(message)
        self.line_numbers = tuple(sorted(set(int(value) for value in line_numbers if value > 0)))


@dataclass(frozen=True)
class InstructionCandidate:
    """Store validated instruction candidate fields used by toolkit reports and adapters."""
    offset: int
    address: int
    size: int
    raw: bytes
    mnemonic: str
    op_str: str
    source: str | None
    label: str | None = None

    @property
    def end(self) -> int:
        """Return the exclusive end offset of this assembly unit."""
        return self.offset + self.size


def _capstone() -> tuple[Any, Any]:
    """Load the Capstone bindings or raise a dependency error."""
    try:
        import capstone  # type: ignore[import-not-found]
        from capstone import x86_const  # type: ignore[import-not-found]
    except ImportError as exc:
        raise ContractError("mnemonic materialization requires the optional capstone dependency") from exc
    return capstone, x86_const


def _safe_symbol(name: str) -> bool:
    """Normalize a symbol name for safe use in generated assembly."""
    return bool(_SAFE_SYMBOL_RE.fullmatch(name))


def _preferred_addresses(
    symbol_map: Mapping[str, SymbolAddress], *, image_base: int
) -> dict[int, str]:
    """Return preferred instruction addresses keyed by source offset."""
    candidates: dict[int, list[str]] = {}
    for name, entry in symbol_map.items():
        if name.startswith("_") and name[1:] in symbol_map:
            continue
        if not _safe_symbol(name):
            continue
        candidates.setdefault(entry.rva, []).append(name)
        candidates.setdefault(image_base + entry.rva, []).append(name)
    result: dict[int, str] = {}
    for address, names in candidates.items():
        result[address] = sorted(names, key=lambda value: (value.startswith("."), len(value), value))[0]
    return result


def _replace_address_token(op_str: str, address: int, symbol: str) -> str | None:
    """Replace one address token with its resolved symbolic form."""
    forms = {
        f"0x{address:x}",
        f"0X{address:X}",
        str(address),
    }
    for form in sorted(forms, key=len, reverse=True):
        if form in op_str:
            return op_str.replace(form, symbol, 1)
    return None


def _instruction_candidates(
    code: bytes,
    *,
    symbol: str,
    base_address: int,
    architecture: str,
    symbol_map: Mapping[str, SymbolAddress],
    image_base: int,
) -> tuple[list[InstructionCandidate], set[str]]:
    """Enumerate candidate instruction encodings for one source unit."""
    capstone, x86_const = _capstone()
    mode = capstone.CS_MODE_32 if architecture == "x86" else capstone.CS_MODE_64
    engine = capstone.Cs(capstone.CS_ARCH_X86, mode)
    engine.detail = True
    decoded = list(engine.disasm(code, base_address))
    if sum(int(insn.size) for insn in decoded) != len(code):
        raise ContractError("Capstone did not decode the complete function; embedded bytes require byte-form output")
    boundaries = {int(insn.address) for insn in decoded}
    local_targets: set[int] = set()
    branch_groups = {capstone.CS_GRP_JUMP, capstone.CS_GRP_CALL}
    for insn in decoded:
        if not any(group in insn.groups for group in branch_groups):
            continue
        if not insn.operands or insn.operands[0].type != x86_const.X86_OP_IMM:
            continue
        target = int(insn.operands[0].imm)
        if base_address <= target < base_address + len(code) and target in boundaries:
            local_targets.add(target)
    address_symbols = _preferred_addresses(symbol_map, image_base=image_base)
    externals: set[str] = set()
    units: list[InstructionCandidate] = []
    for insn in decoded:
        address = int(insn.address)
        offset = address - base_address
        raw = bytes(insn.bytes)
        line: str | None = insn.mnemonic.lower()
        op_str = str(insn.op_str)
        operands = list(insn.operands)
        if any(group in insn.groups for group in branch_groups) and operands:
            operand = operands[0]
            if operand.type == x86_const.X86_OP_IMM:
                target = int(operand.imm)
                if target in local_targets:
                    op_str = f".L_{target:x}"
                else:
                    target_symbol = address_symbols.get(target)
                    if target_symbol is None:
                        line = None
                    else:
                        op_str = target_symbol
                        if target_symbol != symbol:
                            externals.add(target_symbol)
        if line is not None and not any(group in insn.groups for group in branch_groups):
            for operand in operands:
                target: int | None = None
                if operand.type == x86_const.X86_OP_IMM:
                    value = int(operand.imm)
                    if value in address_symbols:
                        target = value
                elif operand.type == x86_const.X86_OP_MEM:
                    memory = operand.mem
                    if architecture == "x86_64" and memory.base == x86_const.X86_REG_RIP:
                        target = address + int(insn.size) + int(memory.disp)
                    elif memory.base == 0 and memory.index == 0:
                        target = int(memory.disp)
                if target is None:
                    continue
                target_symbol = address_symbols.get(target)
                if target_symbol is None:
                    continue
                replaced = _replace_address_token(op_str, target, target_symbol)
                if replaced is None and architecture == "x86_64" and "rip" in op_str:
                    replaced = re.sub(r"\[rip\s*[+-]\s*0x[0-9a-f]+\]", f"[rip + {target_symbol}]", op_str, count=1)
                if replaced is None:
                    line = None
                    break
                op_str = replaced
                if target_symbol != symbol:
                    externals.add(target_symbol)
        if line is not None and op_str:
            line = f"{line} {op_str}"
        units.append(
            InstructionCandidate(
                offset=offset,
                address=address,
                size=int(insn.size),
                raw=raw,
                mnemonic=insn.mnemonic.lower(),
                op_str=str(insn.op_str),
                source=line,
                label=f".L_{address:x}" if address in local_targets else None,
            )
        )
    return units, externals


def _render_source_with_line_map(
    *,
    symbol: str,
    architecture: str,
    units: Sequence[InstructionCandidate],
    fallback_offsets: set[int],
    externals: set[str],
) -> tuple[str, dict[int, int]]:
    """Render source with line map."""
    lines = [
        ".intel_syntax noprefix",
        ".text",
        ".code32" if architecture == "x86" else ".code64",
        ".p2align 0",
        f".globl {symbol}",
    ]
    line_map: dict[int, int] = {}
    for external in sorted(externals):
        if external != symbol:
            lines.append(f".extern {external}")
    lines.append(f"{symbol}:")
    for unit in units:
        if unit.label is not None:
            lines.append(f"{unit.label}:")
        if unit.offset in fallback_offsets or unit.source is None:
            for directive in byte_directive_lines(unit.raw):
                lines.append(directive)
                line_map[len(lines)] = unit.offset
        else:
            lines.append(f"  {unit.source}")
            line_map[len(lines)] = unit.offset
    lines.append("")
    return "\n".join(lines), line_map


def _render_source(
    *,
    symbol: str,
    architecture: str,
    units: Sequence[InstructionCandidate],
    fallback_offsets: set[int],
    externals: set[str],
) -> str:
    """Render source."""
    source, _ = _render_source_with_line_map(
        symbol=symbol,
        architecture=architecture,
        units=units,
        fallback_offsets=fallback_offsets,
        externals=externals,
    )
    return source


def discover_assembler(architecture: str) -> list[str]:
    """Discover assembler."""
    clang = shutil.which("clang")
    if clang is None and sys.platform == "win32":
        candidate = Path("C:/Program Files/LLVM/bin/clang.exe")
        if candidate.is_file():
            clang = str(candidate)
    if clang:
        target = "i686-pc-windows-msvc" if architecture == "x86" else "x86_64-pc-windows-msvc"
        return [clang, f"--target={target}", "-c"]
    names = (
        ["i686-w64-mingw32-gcc", "i686-w64-mingw32-as"]
        if architecture == "x86"
        else ["x86_64-w64-mingw32-gcc", "x86_64-w64-mingw32-as"]
    )
    for name in names:
        executable = shutil.which(name)
        if executable:
            if name.endswith("gcc"):
                return [executable, "-c"]
            return [executable]
    raise ContractError("no COFF-capable assembler found; install clang or a MinGW assembler")


def assemble_coff(
    source_path: Path,
    object_path: Path,
    *,
    architecture: str,
    assembler_command: Sequence[str] | None = None,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    """Assemble generated source into a COFF object with the selected toolchain."""
    command = list(assembler_command or discover_assembler(architecture))
    if not command:
        raise ContractError("assembler command must not be empty")
    object_path.parent.mkdir(parents=True, exist_ok=True)
    command.extend([str(source_path), "-o", str(object_path)])
    completed = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout_seconds,
        check=False,
    )
    if completed.returncode != 0:
        diagnostic = completed.stdout + "\n" + completed.stderr
        escaped = re.escape(str(source_path))
        line_numbers = [
            int(value)
            for value in re.findall(rf"(?:{escaped}|[^\s:]+):(\d+)(?::\d+)?:", diagnostic)
        ]
        raise AssemblerError(
            "assembler failed: "
            + json.dumps(
                {
                    "command": command,
                    "returncode": completed.returncode,
                    "stdout": completed.stdout[-4000:],
                    "stderr": completed.stderr[-4000:],
                },
                sort_keys=True,
            ),
            line_numbers=line_numbers,
        )
    if not object_path.is_file():
        raise ContractError("assembler returned success without producing the requested object")
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "object": str(object_path.resolve()),
    }


def _unit_for_offset(units: Sequence[InstructionCandidate], offset: int) -> InstructionCandidate | None:
    """Return the assembly source unit that contains an output offset."""
    return next((unit for unit in units if unit.offset <= offset < unit.end), None)


def verify_existing_source(
    source_path: Path,
    original_bytes: bytes,
    *,
    symbol: str,
    rva: int,
    architecture: str,
    symbol_map: Mapping[str, Any] | list[Mapping[str, Any]],
    object_path: Path,
    resolved_path: Path | None = None,
    image_base: int = 0,
    assembler_command: Sequence[str] | None = None,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    """Assemble an existing source file and verify its resolved bytes exactly."""
    validate_symbol(symbol)
    if architecture not in {"x86", "x86_64"}:
        raise ContractError("architecture must be x86 or x86_64")
    if not source_path.is_file():
        raise ContractError(f"assembly source does not exist: {source_path}")
    assembly = assemble_coff(
        source_path,
        object_path,
        architecture=architecture,
        assembler_command=assembler_command,
        timeout_seconds=timeout_seconds,
    )
    resolution = RelocationResolver().resolve(
        object_path,
        symbol=symbol,
        base_rva=rva,
        symbol_map=symbol_map,
        image_base=image_base,
        output_path=resolved_path,
        expected_bytes=original_bytes,
    )
    exact = bool(resolution["exact_match"] and not resolution["unresolved_count"])
    return {
        "source": str(source_path.resolve()),
        "source_sha256": sha256_file(source_path),
        "object": str(object_path.resolve()),
        "resolved_output": None if resolved_path is None else str(resolved_path.resolve()),
        "symbol": symbol,
        "rva": rva,
        "architecture": architecture,
        "image_base": image_base,
        "input_sha256": sha256_bytes(original_bytes),
        "resolved_sha256": resolution["resolved_sha256"],
        "exact_match": exact,
        "classification": "exact" if exact else "mismatch",
        "assembly": assembly,
        "resolved_relocation_count": resolution["resolved_count"],
        "unresolved_relocation_count": resolution["unresolved_count"],
        "relocations": resolution["relocations"],
        "semantic_equivalence_claimed": False,
    }


def materialize_function(
    code: bytes,
    *,
    symbol: str,
    rva: int,
    architecture: str,
    symbol_map: Mapping[str, Any] | list[Mapping[str, Any]],
    source_path: Path,
    object_path: Path,
    resolved_path: Path | None = None,
    image_base: int = 0,
    assembler_command: Sequence[str] | None = None,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    """Materialize readable assembly and prove exact bytes, falling back per instruction."""
    validate_symbol(symbol)
    if architecture not in {"x86", "x86_64"}:
        raise ContractError("architecture must be x86 or x86_64")
    if not code:
        raise ContractError("cannot materialize an empty function")
    normalized_map = normalize_symbol_map(symbol_map)
    base_address = image_base + rva
    try:
        units, externals = _instruction_candidates(
            code,
            symbol=symbol,
            base_address=base_address,
            architecture=architecture,
            symbol_map=normalized_map,
            image_base=image_base,
        )
    except ContractError as decode_error:
        # Embedded data or an incomplete instruction stream cannot be rendered as
        # trustworthy mnemonics.  Preserve the complete byte form, assemble it,
        # and still require an exact round trip before reporting success.
        source_path.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_bytes(
            source_path, render_byte_assembly(symbol, code, architecture).encode("utf-8")
        )
        assembly = assemble_coff(
            source_path,
            object_path,
            architecture=architecture,
            assembler_command=assembler_command,
            timeout_seconds=timeout_seconds,
        )
        resolution = RelocationResolver().resolve(
            object_path,
            symbol=symbol,
            base_rva=rva,
            symbol_map=symbol_map,
            image_base=image_base,
            output_path=resolved_path,
            expected_bytes=code,
        )
        if not resolution["exact_match"] or resolution["unresolved_count"]:
            raise ContractError("byte-form fallback failed exact round-trip verification")
        return {
            "format": "mnemonic",
            "symbol": symbol,
            "rva": rva,
            "base_address": base_address,
            "architecture": architecture,
            "input_sha256": sha256_bytes(code),
            "source": str(source_path.resolve()),
            "object": str(object_path.resolve()),
            "resolved_output": None if resolved_path is None else str(resolved_path.resolve()),
            "resolved_sha256": resolution["resolved_sha256"],
            "instruction_count": 0,
            "mnemonic_count": 0,
            "byte_escape_count": len(code),
            "byte_escape_bytes": len(code),
            "relocation_count": len(resolution["relocations"]),
            "resolved_relocation_count": resolution["resolved_count"],
            "unresolved_relocation_count": resolution["unresolved_count"],
            "exact_match": True,
            "classification": "byte-form-fallback",
            "fallback_offsets": [0],
            "attempts": [{"attempt": 1, "decode_error": str(decode_error), "assembly": assembly}],
            "relocations": resolution["relocations"],
            "semantic_equivalence_claimed": False,
        }
    fallback_offsets = {unit.offset for unit in units if unit.source is None}
    attempts: list[dict[str, Any]] = []
    resolver = RelocationResolver()
    max_attempts = len(units) + 2
    source_path.parent.mkdir(parents=True, exist_ok=True)
    object_path.parent.mkdir(parents=True, exist_ok=True)
    last_resolution: dict[str, Any] | None = None
    for attempt_number in range(1, max_attempts + 1):
        rendered, line_map = _render_source_with_line_map(
            symbol=symbol,
            architecture=architecture,
            units=units,
            fallback_offsets=fallback_offsets,
            externals=externals,
        )
        atomic_write_bytes(source_path, rendered.encode("utf-8"))
        try:
            assembly = assemble_coff(
                source_path,
                object_path,
                architecture=architecture,
                assembler_command=assembler_command,
                timeout_seconds=timeout_seconds,
            )
            resolution = resolver.resolve(
                object_path,
                symbol=symbol,
                base_rva=rva,
                symbol_map=symbol_map,
                image_base=image_base,
                expected_bytes=code,
            )
            last_resolution = resolution
            unresolved_offsets = {
                int(item["offset"])
                for item in resolution["relocations"]
                if item["status"] != "resolved"
            }
            attempts.append(
                {
                    "attempt": attempt_number,
                    "fallback_count": len(fallback_offsets),
                    "assembly": assembly,
                    "unresolved_offsets": sorted(unresolved_offsets),
                    "exact_match": resolution["exact_match"],
                }
            )
            if not unresolved_offsets and resolution["exact_match"]:
                break
            new_fallbacks = set()
            for offset in unresolved_offsets:
                unit = _unit_for_offset(units, offset)
                if unit is not None:
                    new_fallbacks.add(unit.offset)
            if not new_fallbacks:
                resolved = bytes(resolution["resolved_bytes"])
                common = min(len(code), len(resolved))
                mismatch = next(
                    (index for index in range(common) if code[index] != resolved[index]),
                    common,
                )
                unit = _unit_for_offset(units, mismatch)
                if unit is not None:
                    new_fallbacks.add(unit.offset)
                elif len(code) != len(resolved):
                    new_fallbacks.update(
                        unit.offset for unit in units if unit.offset not in fallback_offsets
                    )
            before = len(fallback_offsets)
            fallback_offsets.update(new_fallbacks)
            if len(fallback_offsets) == before:
                fallback_offsets.update(unit.offset for unit in units)
        except AssemblerError as exc:
            focused = {
                line_map[line]
                for line in exc.line_numbers
                if line in line_map and line_map[line] not in fallback_offsets
            }
            attempts.append(
                {
                    "attempt": attempt_number,
                    "fallback_count": len(fallback_offsets),
                    "error": str(exc),
                    "diagnostic_lines": list(exc.line_numbers),
                    "focused_fallbacks": sorted(focused),
                }
            )
            if focused:
                fallback_offsets.update(focused)
                continue
            remaining = [unit.offset for unit in units if unit.offset not in fallback_offsets]
            if not remaining:
                raise
            # Without a usable line diagnostic, fall back conservatively.  Exact
            # round-trip verification still governs acceptance.
            fallback_offsets.update(remaining)
        except ContractError as exc:
            attempts.append(
                {
                    "attempt": attempt_number,
                    "fallback_count": len(fallback_offsets),
                    "error": str(exc),
                }
            )
            remaining = [unit.offset for unit in units if unit.offset not in fallback_offsets]
            if not remaining:
                raise
            fallback_offsets.update(remaining)
    if last_resolution is None or not last_resolution["exact_match"] or last_resolution["unresolved_count"]:
        raise ContractError("failed to produce exact relocation-resolved bytes even after byte fallback")
    final_bytes = bytes(last_resolution["resolved_bytes"])
    if resolved_path is not None:
        atomic_write_bytes(resolved_path, final_bytes)
    mnemonic_count = sum(
        1 for unit in units if unit.offset not in fallback_offsets and unit.source is not None
    )
    byte_escape_count = len(units) - mnemonic_count
    classification = (
        "fully-mnemonic"
        if byte_escape_count == 0
        else "byte-form-fallback"
        if mnemonic_count == 0
        else "mixed-mnemonic-byte"
    )
    return {
        "format": "mnemonic",
        "symbol": symbol,
        "rva": rva,
        "base_address": base_address,
        "architecture": architecture,
        "input_sha256": sha256_bytes(code),
        "source": str(source_path.resolve()),
        "object": str(object_path.resolve()),
        "resolved_output": None if resolved_path is None else str(resolved_path.resolve()),
        "resolved_sha256": sha256_bytes(final_bytes),
        "instruction_count": len(units),
        "mnemonic_count": mnemonic_count,
        "byte_escape_count": byte_escape_count,
        "byte_escape_bytes": sum(
            len(unit.raw) for unit in units if unit.offset in fallback_offsets or unit.source is None
        ),
        "relocation_count": len(last_resolution["relocations"]),
        "resolved_relocation_count": last_resolution["resolved_count"],
        "unresolved_relocation_count": last_resolution["unresolved_count"],
        "exact_match": True,
        "classification": classification,
        "fallback_offsets": sorted(fallback_offsets),
        "attempts": attempts,
        "relocations": last_resolution["relocations"],
        "semantic_equivalence_claimed": False,
    }

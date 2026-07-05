"""Independent Capstone-backed x86/x86-64 decoding and normalization."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .errors import ContractError, ExternalToolError
from .util import sha256_bytes, utc_now, write_json


def _capstone() -> Any:
    """Implement capstone.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    try:
        import capstone  # type: ignore
        from capstone import x86_const  # type: ignore
    except ImportError as exc:
        raise ExternalToolError(
            "Capstone is required for instruction decoding; install x86decomp-toolkit[disassembly]"
        ) from exc
    return capstone, x86_const


@dataclass(frozen=True)
class InstructionRecord:
    """Store the validated fields for instruction record records.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    address: int
    offset: int
    size: int
    bytes_hex: str
    mnemonic: str
    op_str: str
    normalized: str
    branch_target: int | None
    fallthrough: int | None

    def to_dict(self) -> dict[str, Any]:
        """Convert dict.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return {
            "address": self.address,
            "address_hex": f"0x{self.address:x}",
            "offset": self.offset,
            "size": self.size,
            "bytes_hex": self.bytes_hex,
            "mnemonic": self.mnemonic,
            "op_str": self.op_str,
            "normalized": self.normalized,
            "branch_target": self.branch_target,
            "fallthrough": self.fallthrough,
        }


def _is_known_address(value: int, ranges: Iterable[tuple[int, int]]) -> bool:
    """Implement is known address.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return any(start <= value < end for start, end in ranges)


def decode_instructions(
    code: bytes,
    *,
    base_address: int,
    architecture: str = "x86",
    known_address_ranges: Iterable[tuple[int, int]] = (),
) -> list[InstructionRecord]:
    """Decode instructions.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if architecture not in ("x86", "x86_64"):
        raise ContractError("architecture must be x86 or x86_64")
    capstone, x86_const = _capstone()
    mode = capstone.CS_MODE_32 if architecture == "x86" else capstone.CS_MODE_64
    engine = capstone.Cs(capstone.CS_ARCH_X86, mode)
    engine.detail = True
    records: list[InstructionRecord] = []
    code_end = base_address + len(code)
    branch_groups = {capstone.CS_GRP_JUMP, capstone.CS_GRP_CALL}
    stop_group = capstone.CS_GRP_RET
    for instruction in engine.disasm(code, base_address):
        normalized_operands: list[str] = []
        direct_target: int | None = None
        for operand in instruction.operands:
            if operand.type == x86_const.X86_OP_REG:
                normalized_operands.append(engine.reg_name(operand.reg))
            elif operand.type == x86_const.X86_OP_IMM:
                value = int(operand.imm)
                if any(group in instruction.groups for group in branch_groups):
                    direct_target = value
                    if base_address <= value < code_end:
                        normalized_operands.append(f"loc_{value - base_address:x}")
                    else:
                        normalized_operands.append("external_target")
                elif _is_known_address(value, known_address_ranges):
                    normalized_operands.append("known_address")
                else:
                    normalized_operands.append(f"imm:{value:#x}")
            elif operand.type == x86_const.X86_OP_MEM:
                memory = operand.mem
                base = engine.reg_name(memory.base) if memory.base else ""
                index = engine.reg_name(memory.index) if memory.index else ""
                scale = int(memory.scale)
                displacement = int(memory.disp)
                if base in ("ebp", "esp", "rbp", "rsp"):
                    disp = f"{displacement:+#x}"
                elif base == "rip":
                    target = instruction.address + instruction.size + displacement
                    disp = (
                        f"loc_{target - base_address:x}"
                        if base_address <= target < code_end
                        else "external_rip_address"
                    )
                elif not base and not index and _is_known_address(displacement, known_address_ranges):
                    disp = "known_address"
                elif not base and not index:
                    disp = "absolute_address"
                else:
                    disp = f"{displacement:+#x}"
                normalized_operands.append(
                    f"mem:{base or '-'}:{index or '-'}:{scale}:{disp}:size{operand.size}"
                )
            else:
                normalized_operands.append(f"operand_type:{operand.type}")
        normalized = instruction.mnemonic.lower()
        if normalized_operands:
            normalized += " " + ",".join(normalized_operands)
        is_unconditional_jump = instruction.mnemonic.lower() == "jmp"
        is_return = stop_group in instruction.groups
        fallthrough = None if is_unconditional_jump or is_return else instruction.address + instruction.size
        records.append(
            InstructionRecord(
                address=instruction.address,
                offset=instruction.address - base_address,
                size=instruction.size,
                bytes_hex=bytes(instruction.bytes).hex(),
                mnemonic=instruction.mnemonic.lower(),
                op_str=instruction.op_str,
                normalized=normalized,
                branch_target=direct_target,
                fallthrough=fallthrough,
            )
        )
    decoded_size = sum(record.size for record in records)
    if decoded_size != len(code):
        raise ContractError(
            f"Capstone decoded {decoded_size} of {len(code)} bytes; undecoded or embedded data is present"
        )
    return records


def control_flow_edges(records: list[InstructionRecord], *, base_address: int, code_size: int) -> list[tuple[int, int, str]]:
    """Implement control flow edges.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    code_end = base_address + code_size
    edges: set[tuple[int, int, str]] = set()
    for record in records:
        source = record.offset
        if record.branch_target is not None and base_address <= record.branch_target < code_end:
            kind = "call" if record.mnemonic == "call" else "branch"
            edges.add((source, record.branch_target - base_address, kind))
        if record.fallthrough is not None and record.fallthrough < code_end:
            edges.add((source, record.fallthrough - base_address, "fallthrough"))
    return sorted(edges)


def compare_instruction_streams(
    target: bytes,
    candidate: bytes,
    *,
    target_base: int,
    candidate_base: int = 0,
    architecture: str = "x86",
    target_known_ranges: Iterable[tuple[int, int]] = (),
    candidate_known_ranges: Iterable[tuple[int, int]] = (),
) -> dict[str, Any]:
    """Compare instruction streams.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    from difflib import SequenceMatcher

    target_records = decode_instructions(
        target,
        base_address=target_base,
        architecture=architecture,
        known_address_ranges=target_known_ranges,
    )
    candidate_records = decode_instructions(
        candidate,
        base_address=candidate_base,
        architecture=architecture,
        known_address_ranges=candidate_known_ranges,
    )
    target_tokens = [record.normalized for record in target_records]
    candidate_tokens = [record.normalized for record in candidate_records]
    matcher = SequenceMatcher(None, target_tokens, candidate_tokens, autojunk=False)
    operations = [
        {
            "tag": tag,
            "target": [i1, i2],
            "candidate": [j1, j2],
            "target_tokens": target_tokens[i1:i2],
            "candidate_tokens": candidate_tokens[j1:j2],
        }
        for tag, i1, i2, j1, j2 in matcher.get_opcodes()
        if tag != "equal"
    ]
    target_edges = control_flow_edges(target_records, base_address=target_base, code_size=len(target))
    candidate_edges = control_flow_edges(
        candidate_records, base_address=candidate_base, code_size=len(candidate)
    )
    return {
        "schema_version": 1,
        "created_at": utc_now(),
        "architecture": architecture,
        "target_sha256": sha256_bytes(target),
        "candidate_sha256": sha256_bytes(candidate),
        "target_instruction_count": len(target_records),
        "candidate_instruction_count": len(candidate_records),
        "normalized_similarity": matcher.ratio(),
        "normalized_equal": target_tokens == candidate_tokens,
        "cfg_equal": target_edges == candidate_edges,
        "target_cfg_edges": [list(edge) for edge in target_edges],
        "candidate_cfg_edges": [list(edge) for edge in candidate_edges],
        "differences": operations,
        "target_instructions": [record.to_dict() for record in target_records],
        "candidate_instructions": [record.to_dict() for record in candidate_records],
        "semantic_equivalence_claimed": False,
    }


def cross_check_ghidra_instructions(
    ghidra_jsonl: Path,
    code: bytes,
    *,
    base_address: int,
    architecture: str = "x86",
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Implement cross check ghidra instructions.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    records = decode_instructions(code, base_address=base_address, architecture=architecture)
    ghidra: list[dict[str, Any]] = []
    with ghidra_jsonl.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ContractError(f"invalid Ghidra JSONL line {line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise ContractError(f"Ghidra JSONL line {line_number} must be an object")
            ghidra.append(value)
    discrepancies: list[dict[str, Any]] = []
    count = max(len(ghidra), len(records))
    for index in range(count):
        if index >= len(ghidra):
            discrepancies.append({"index": index, "kind": "missing_in_ghidra"})
            continue
        if index >= len(records):
            discrepancies.append({"index": index, "kind": "missing_in_capstone"})
            continue
        left = ghidra[index]
        right = records[index]
        ghidra_bytes = str(left.get("bytes_hex", "")).lower().replace(" ", "")
        ghidra_mnemonic = str(left.get("mnemonic", "")).lower()
        if ghidra_bytes != right.bytes_hex or ghidra_mnemonic != right.mnemonic:
            discrepancies.append(
                {
                    "index": index,
                    "kind": "decode_mismatch",
                    "ghidra": {"bytes_hex": ghidra_bytes, "mnemonic": ghidra_mnemonic},
                    "capstone": {"bytes_hex": right.bytes_hex, "mnemonic": right.mnemonic},
                }
            )
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "architecture": architecture,
        "ghidra_instruction_count": len(ghidra),
        "capstone_instruction_count": len(records),
        "consistent": not discrepancies,
        "discrepancies": discrepancies,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report

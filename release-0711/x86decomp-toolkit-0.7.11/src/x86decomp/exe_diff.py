"""Executable-function versus COFF-symbol comparison for matching mode."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .coff import CoffRelocation, extract_symbol, parse_coff
from .diffing import compare_bytes
from .disassembly import compare_instruction_streams
from .errors import ContractError, FormatError
from .pe import parse_pe
from .util import sha256_bytes, utc_now, write_json


def rva_to_file_offset(image: Any, rva: int) -> int:
    """Translate an RVA to a validated file offset in a PE image."""
    if rva < 0:
        raise ContractError("RVA must be non-negative")
    if rva < image.size_of_headers:
        return rva
    for section in image.sections:
        start = section.virtual_address
        end = start + max(section.virtual_size, section.raw_size)
        if start <= rva < end:
            delta = rva - start
            if delta >= section.raw_size:
                raise FormatError(f"RVA 0x{rva:x} is in the zero-filled tail of {section.name}")
            return section.raw_offset + delta
    raise FormatError(f"RVA 0x{rva:x} is not mapped by the PE image")


def extract_pe_bytes(path: Path, *, rva: int, size: int) -> tuple[Any, bytes]:
    """Extract PE bytes."""
    if size <= 0:
        raise ContractError("PE extraction size must be positive")
    image = parse_pe(path)
    offset = rva_to_file_offset(image, rva)
    data = path.read_bytes()
    if offset + size > len(data):
        raise FormatError("requested PE function range exceeds file bounds")
    # Do not silently cross into another section or a non-raw region.
    for section in image.sections:
        if section.raw_offset <= offset < section.raw_offset + section.raw_size:
            if offset + size > section.raw_offset + section.raw_size:
                raise FormatError("requested PE function range crosses a section raw-data boundary")
            break
    return image, data[offset : offset + size]


def _masked_copy(data: bytes, masks: list[tuple[int, int, str]]) -> bytes:
    """Return a byte copy with relocation-sensitive ranges normalized to zero."""
    result = bytearray(data)
    for offset, width, _reason in masks:
        if offset < 0 or width <= 0 or offset + width > len(result):
            raise ContractError(f"normalization mask [{offset}, {offset + width}) exceeds function bytes")
        result[offset : offset + width] = b"\x00" * width
    return bytes(result)


def _candidate_relocation_masks(relocations: tuple[CoffRelocation, ...], machine: int) -> list[tuple[int, int, str]]:
    """Build candidate-byte mask ranges from COFF relocation records."""
    masks: list[tuple[int, int, str]] = []
    for relocation in relocations:
        width = relocation.width(machine)
        if width is None:
            continue
        masks.append(
            (
                relocation.offset,
                width,
                f"coff:0x{relocation.type:04x}:{relocation.symbol_name or relocation.symbol_index}",
            )
        )
    return masks


def _pe_base_relocation_masks(image: Any, *, function_rva: int, size: int) -> list[tuple[int, int, str]]:
    """Build target-byte mask ranges from PE base relocations inside a function."""
    masks: list[tuple[int, int, str]] = []
    for relocation in image.base_relocations:
        if function_rva <= relocation.rva < function_rva + size:
            width = 4 if relocation.type == 3 else 8 if relocation.type == 10 else None  # HIGHLOW / DIR64
            if width is not None and relocation.rva + width <= function_rva + size:
                masks.append((relocation.rva - function_rva, width, "pe-base-relocation"))
    return masks


def compare_pe_function_to_coff_symbol(
    *,
    pe_path: Path,
    function_rva: int,
    function_size: int,
    coff_path: Path,
    symbol_name: str,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Compare PE function to COFF symbol."""
    image, target = extract_pe_bytes(pe_path, rva=function_rva, size=function_size)
    obj = parse_coff(coff_path)
    expected_machine = image.machine
    if obj.machine != expected_machine:
        raise ContractError(
            f"architecture mismatch: PE machine=0x{image.machine:04x}, COFF machine=0x{obj.machine:04x}"
        )
    extracted = extract_symbol(obj, symbol_name, size=None)
    candidate = extracted.data
    raw = compare_bytes(target, candidate)

    candidate_masks = _candidate_relocation_masks(extracted.relocations, obj.machine)
    pe_masks = _pe_base_relocation_masks(image, function_rva=function_rva, size=function_size)
    # Candidate relocations identify operand locations whose final values are linker-dependent.
    # Apply the same locations to the linked target only when the range exists.
    aligned_masks = [mask for mask in candidate_masks if mask[0] + mask[1] <= len(target)]
    target_masks = {(offset, width): reason for offset, width, reason in pe_masks}
    for offset, width, reason in aligned_masks:
        target_masks[(offset, width)] = reason
    candidate_mask_keys = {(offset, width) for offset, width, _ in candidate_masks}
    all_mask_keys = sorted(set(target_masks) | candidate_mask_keys)
    shared_masks = [
        (offset, width, target_masks.get((offset, width), "coff-relocation"))
        for offset, width in all_mask_keys
        if offset + width <= len(target) and offset + width <= len(candidate)
    ]
    target_normalized = _masked_copy(target, shared_masks)
    candidate_normalized = _masked_copy(candidate, shared_masks)
    normalized_bytes = compare_bytes(target_normalized, candidate_normalized)

    architecture = "x86" if obj.machine == 0x014C else "x86_64"
    instruction_error: str | None = None
    instruction_report: dict[str, Any] | None
    try:
        ranges = [
            (image.image_base + section.virtual_address, image.image_base + section.virtual_address + section.mapped_size)
            for section in image.sections
        ]
        instruction_report = compare_instruction_streams(
            target,
            candidate,
            target_base=image.image_base + function_rva,
            candidate_base=0,
            architecture=architecture,
            target_known_ranges=ranges,
        )
    except Exception as exc:
        instruction_report = None
        instruction_error = str(exc)

    if raw["equal"]:
        classification = "byte_matched"
    elif normalized_bytes["equal"]:
        classification = "relocation_normalized_match"
    elif instruction_report is not None and instruction_report["normalized_equal"]:
        classification = "instruction_similar"
    else:
        classification = "mismatch"

    report = {
        "schema_version": 2,
        "created_at": utc_now(),
        "kind": "pe_function_vs_coff_symbol",
        "architecture": architecture,
        "classification": classification,
        "pe": {
            "path": str(pe_path.resolve()),
            "file_sha256": image.file_sha256,
            "function_rva": function_rva,
            "function_va": image.image_base + function_rva,
            "function_size": function_size,
            "function_sha256": sha256_bytes(target),
        },
        "coff": {
            "path": str(coff_path.resolve()),
            "object_sha256": obj.raw_sha256,
            "symbol": extracted.to_dict(obj.machine),
        },
        "normalization_masks": [
            {"offset": offset, "width": width, "reason": reason}
            for offset, width, reason in shared_masks
        ],
        "raw_byte_comparison": raw,
        "normalized_byte_comparison": normalized_bytes,
        "instruction_comparison": instruction_report,
        "instruction_comparison_error": instruction_error,
        "semantic_equivalence_claimed": False,
        "limitations": [
            "Relocation-normalized equality is not raw byte equality.",
            "Instruction similarity is not semantic equivalence.",
            "Linked PE images do not retain all original COFF relocation records.",
        ],
    }
    if report_path is not None:
        write_json(report_path, report)
    return report

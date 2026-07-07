"""Target-specific whole-image matching and deterministic normalization.

A layout profile records which PE fields are expected to match exactly and which
build-produced fields may be normalized.  The matcher never promotes a
normalized match to an exact byte-identical match.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .errors import ContractError, FormatError
from .pe import parse_pe
from .util import load_json, sha256_file, utc_now, write_json


@dataclass(frozen=True)
class ByteRange:
    """Store validated byte range fields used by toolkit reports and adapters."""
    start: int
    end: int
    reason: str

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {"start": self.start, "end": self.end, "reason": self.reason}


def _pe_offsets(data: bytes) -> dict[str, int]:
    """Compute file offsets of PE fields relevant to whole-image matching.

    Args:
        data: Raw PE image bytes.

    Returns:
        A dict of file offsets for the PE header, COFF timestamp, optional header,
        checksum, data-directory base, and the certificate and debug directory entries.

    Raises:
        FormatError: If the MZ or PE signatures are missing, or the optional-header
            magic is not PE32/PE32+.
    """
    if len(data) < 0x40 or data[:2] != b"MZ":
        raise FormatError("missing DOS MZ signature")
    pe = struct.unpack_from("<I", data, 0x3C)[0]
    if pe + 24 > len(data) or data[pe : pe + 4] != b"PE\x00\x00":
        raise FormatError("missing PE signature")
    optional = pe + 24
    magic = struct.unpack_from("<H", data, optional)[0]
    if magic not in (0x10B, 0x20B):
        raise FormatError(f"unsupported optional-header magic 0x{magic:04x}")
    directory_base = optional + (96 if magic == 0x10B else 112)
    return {
        "pe": pe,
        "coff_timestamp": pe + 8,
        "optional": optional,
        "checksum": optional + 64,
        "directory_base": directory_base,
        "certificate_directory": directory_base + 4 * 8,
        "debug_directory": directory_base + 6 * 8,
    }


def derive_layout_profile(reference: Path, *, output: Path | None = None) -> dict[str, Any]:
    """Derive a target-specific layout profile from a reference PE image.

    Captures the reference's architecture, alignments, section layout and order, and
    default normalization flags (only the PE checksum normalized by default).

    Args:
        reference: Path to the reference PE image.
        output: Optional path to write the derived profile JSON to.

    Returns:
        The derived layout profile dict.
    """
    image = parse_pe(reference)
    profile = {
        "schema_version": 1,
        "kind": "target_specific_image_profile",
        "reference_sha256": image.file_sha256,
        "architecture": image.to_dict()["architecture"],
        "image_base": image.image_base,
        "entry_rva": image.entry_rva,
        "section_alignment": image.section_alignment,
        "file_alignment": image.file_alignment,
        "subsystem": image.subsystem,
        "dll_characteristics": image.dll_characteristics,
        "section_order": [section.name for section in image.sections],
        "sections": [
            {
                "name": section.name,
                "virtual_address": section.virtual_address,
                "virtual_size": section.virtual_size,
                "raw_offset": section.raw_offset,
                "raw_size": section.raw_size,
                "characteristics": section.characteristics,
            }
            for section in image.sections
        ],
        "normalization": {
            "coff_timestamp": False,
            "checksum": True,
            "certificate_directory_entry": False,
            "debug_directory_records": False,
            "rebase_candidate": False,
            "extra_ranges": [],
        },
    }
    if output is not None:
        write_json(output, profile)
    return profile


def _mask_ranges(data: bytes, ranges: Iterable[ByteRange]) -> bytes:
    """Zero out the given byte ranges in a copy of the image.

    Args:
        data: Raw image bytes.
        ranges: Byte ranges to mask (set to NUL).

    Returns:
        A new bytes object with each range zeroed.

    Raises:
        ContractError: If any range is negative, inverted, or extends past the image.
    """
    result = bytearray(data)
    for item in ranges:
        if item.start < 0 or item.end < item.start or item.end > len(result):
            raise ContractError(f"normalization range outside image: {item}")
        result[item.start : item.end] = b"\x00" * (item.end - item.start)
    return bytes(result)


def _rva_to_file_offset(image: Any, rva: int, file_size: int) -> int | None:
    """Translate an RVA to a file offset using the image's headers and sections.

    Args:
        image: Parsed PE image providing sections and header size.
        rva: Relative virtual address to translate.
        file_size: Total file size, used to bound the resulting offset.

    Returns:
        The corresponding file offset, or None if the RVA maps outside the file.
    """
    if rva < image.size_of_headers and rva < file_size:
        return rva
    for section in image.sections:
        if section.virtual_address <= rva < section.virtual_address + section.mapped_size:
            offset = section.raw_offset + rva - section.virtual_address
            return offset if 0 <= offset < file_size else None
    return None


def _profile_ranges(data: bytes, profile: dict[str, Any], image: Any) -> list[ByteRange]:
    """Compute the byte ranges to normalize for an image per a layout profile.

    Adds ranges for the COFF timestamp, PE checksum, certificate directory, debug
    directory records and payloads, and any profile-supplied extra ranges, according
    to the profile's normalization flags.

    Args:
        data: Raw image bytes.
        profile: Layout profile with a ``normalization`` object.
        image: Parsed PE image used to resolve debug directory locations.

    Returns:
        The list of byte ranges to mask.

    Raises:
        ContractError: If ``normalization`` or ``extra_ranges`` is malformed, or a
            debug directory/payload range falls outside the image.
    """
    offsets = _pe_offsets(data)
    normalization = profile.get("normalization", {})
    if not isinstance(normalization, dict):
        raise ContractError("profile normalization must be an object")
    ranges: list[ByteRange] = []
    if normalization.get("coff_timestamp", False):
        ranges.append(ByteRange(offsets["coff_timestamp"], offsets["coff_timestamp"] + 4, "coff_timestamp"))
    if normalization.get("checksum", True):
        ranges.append(ByteRange(offsets["checksum"], offsets["checksum"] + 4, "pe_checksum"))
    if normalization.get("certificate_directory_entry", False):
        ranges.append(ByteRange(offsets["certificate_directory"], offsets["certificate_directory"] + 8, "certificate_directory"))
    if normalization.get("debug_directory_records", False):
        debug_directory = next((item for item in image.directories if item.name == "debug"), None)
        if debug_directory is not None and debug_directory.rva and debug_directory.size:
            directory_offset = _rva_to_file_offset(image, debug_directory.rva, len(data))
            if directory_offset is None or directory_offset + debug_directory.size > len(data):
                raise ContractError("debug directory normalization range is outside image")
            ranges.append(ByteRange(directory_offset, directory_offset + debug_directory.size, "debug_directory_records"))
        for index, record in enumerate(image.debug_records):
            if record.raw_data_offset and record.size_of_data:
                end = record.raw_data_offset + record.size_of_data
                if end > len(data):
                    raise ContractError("debug payload normalization range is outside image")
                ranges.append(ByteRange(record.raw_data_offset, end, f"debug_payload_{index}"))
    extra = normalization.get("extra_ranges", [])
    if not isinstance(extra, list):
        raise ContractError("normalization.extra_ranges must be an array")
    for item in extra:
        if not isinstance(item, dict):
            raise ContractError("normalization range must be an object")
        ranges.append(ByteRange(int(item["start"]), int(item["end"]), str(item.get("reason", "profile"))))
    return ranges


def _apply_rebase(data: bytes, *, target_base: int, candidate_base: int, image: Any) -> bytes:
    """Rebase a candidate image's absolute addresses to a target image base.

    Applies the base relocations (types 3 and 10) by adding the base delta to each
    relocated 4- or 8-byte value; returns the input unchanged when the delta is zero.

    Args:
        data: Raw candidate image bytes.
        target_base: Image base of the reference image.
        candidate_base: Image base of the candidate image.
        image: Parsed candidate PE image providing base relocations and sections.

    Returns:
        The rebased image bytes.
    """
    delta = target_base - candidate_base
    if delta == 0:
        return data
    result = bytearray(data)
    for relocation in image.base_relocations:
        if relocation.type not in (3, 10):
            continue
        section = next(
            (
                item
                for item in image.sections
                if item.virtual_address <= relocation.rva < item.virtual_address + item.mapped_size
            ),
            None,
        )
        if section is None:
            continue
        file_offset = section.raw_offset + relocation.rva - section.virtual_address
        width = 4 if relocation.type == 3 else 8
        if file_offset < 0 or file_offset + width > len(result):
            continue
        value = int.from_bytes(result[file_offset : file_offset + width], "little")
        mask = (1 << (width * 8)) - 1
        result[file_offset : file_offset + width] = ((value + delta) & mask).to_bytes(width, "little")
    return bytes(result)


def _mismatches(left: bytes, right: bytes, limit: int = 256) -> tuple[int, list[dict[str, int]]]:
    """Count differing bytes between two buffers and collect example offsets.

    Compares byte by byte over the longer length, treating missing bytes as ``-1``.

    Args:
        left: First buffer (reported as ``reference``).
        right: Second buffer (reported as ``candidate``).
        limit: Maximum number of example mismatches to record. Defaults to 256.

    Returns:
        A tuple of the total mismatch count and up to ``limit`` example records, each
        with the offset and the reference and candidate byte values.
    """
    count = 0
    examples: list[dict[str, int]] = []
    for offset in range(max(len(left), len(right))):
        a = left[offset] if offset < len(left) else -1
        b = right[offset] if offset < len(right) else -1
        if a != b:
            count += 1
            if len(examples) < limit:
                examples.append({"offset": offset, "reference": a, "candidate": b})
    return count, examples


def compare_whole_images(
    reference: Path,
    candidate: Path,
    *,
    profile_path: Path | None = None,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Compare a candidate PE image against a reference under a layout profile.

    Derives or loads a layout profile, optionally rebases the candidate, masks the
    profile's normalization ranges, and reports raw and normalized mismatch counts
    plus per-section layout and byte comparisons. A normalized match is never
    promoted to a byte-identical claim.

    Args:
        reference: Path to the reference PE image.
        candidate: Path to the candidate PE image.
        profile_path: Optional layout profile; when omitted a default is derived from
            the reference.
        report_path: Optional path to write the comparison report to.

    Returns:
        A whole-image match report dict whose ``classification`` is
        ``byte_identical``, ``profile_normalized_match``, or ``different``.

    Raises:
        ContractError: If an input image is missing, the profile is not an object, or
            the profile's reference hash does not match the supplied reference.
    """
    if not reference.is_file() or not candidate.is_file():
        raise ContractError("reference and candidate images must exist")
    reference_data = reference.read_bytes()
    candidate_data = candidate.read_bytes()
    reference_image = parse_pe(reference)
    candidate_image = parse_pe(candidate)
    if profile_path is None:
        profile = derive_layout_profile(reference)
        profile_source = "derived_default"
    else:
        profile = load_json(profile_path)
        if not isinstance(profile, dict):
            raise ContractError("layout profile must be an object")
        profile_source = str(profile_path.resolve())
    expected_hash = profile.get("reference_sha256")
    if expected_hash is not None and expected_hash != sha256_file(reference):
        raise ContractError("layout profile reference hash does not match supplied reference image")
    normalization = profile.get("normalization", {})
    normalized_candidate = candidate_data
    if isinstance(normalization, dict) and normalization.get("rebase_candidate", False):
        normalized_candidate = _apply_rebase(
            normalized_candidate,
            target_base=reference_image.image_base,
            candidate_base=candidate_image.image_base,
            image=candidate_image,
        )
    ranges_reference = _profile_ranges(reference_data, profile, reference_image)
    ranges_candidate = _profile_ranges(normalized_candidate, profile, candidate_image)
    normalized_reference = _mask_ranges(reference_data, ranges_reference)
    normalized_candidate = _mask_ranges(normalized_candidate, ranges_candidate)
    raw_count, raw_examples = _mismatches(reference_data, candidate_data)
    normalized_count, normalized_examples = _mismatches(normalized_reference, normalized_candidate)

    expected_order = profile.get("section_order")
    actual_order = [section.name for section in candidate_image.sections]
    section_order_match = not isinstance(expected_order, list) or actual_order == expected_order
    section_reports: list[dict[str, Any]] = []
    reference_sections = {section.name: section for section in reference_image.sections}
    candidate_sections = {section.name: section for section in candidate_image.sections}
    for name in sorted(set(reference_sections) | set(candidate_sections)):
        left = reference_sections.get(name)
        right = candidate_sections.get(name)
        if left is None or right is None:
            section_reports.append({"name": name, "present_in_both": False})
            continue
        left_bytes = reference_data[left.raw_offset : left.raw_offset + left.raw_size]
        right_bytes = candidate_data[right.raw_offset : right.raw_offset + right.raw_size]
        count, examples = _mismatches(left_bytes, right_bytes, limit=32)
        section_reports.append(
            {
                "name": name,
                "present_in_both": True,
                "layout_match": (
                    left.virtual_address, left.virtual_size, left.raw_offset, left.raw_size, left.characteristics
                ) == (
                    right.virtual_address, right.virtual_size, right.raw_offset, right.raw_size, right.characteristics
                ),
                "reference_raw_offset": left.raw_offset,
                "candidate_raw_offset": right.raw_offset,
                "reference_raw_size": left.raw_size,
                "candidate_raw_size": right.raw_size,
                "byte_mismatch_count": count,
                "examples": examples,
            }
        )
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "target_specific_whole_image_match",
        "reference": {"path": str(reference.resolve()), "sha256": sha256_file(reference)},
        "candidate": {"path": str(candidate.resolve()), "sha256": sha256_file(candidate)},
        "profile_source": profile_source,
        "profile": profile,
        "raw_exact_match": raw_count == 0,
        "raw_mismatch_count": raw_count,
        "raw_mismatches": raw_examples,
        "normalized_match": normalized_count == 0,
        "normalized_mismatch_count": normalized_count,
        "normalized_mismatches": normalized_examples,
        "normalization_ranges": [item.to_dict() for item in ranges_reference],
        "section_order_match": section_order_match,
        "sections": section_reports,
        "classification": "byte_identical"
        if raw_count == 0
        else "profile_normalized_match"
        if normalized_count == 0
        else "different",
        "universal_equivalence_claimed": False,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report

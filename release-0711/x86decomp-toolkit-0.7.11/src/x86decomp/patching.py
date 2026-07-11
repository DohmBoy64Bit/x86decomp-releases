"""Patch-image backend with integrity checks and PE checksum refresh."""

from __future__ import annotations

import struct
from pathlib import Path
from typing import Any

from .errors import ContractError
from .exe_diff import rva_to_file_offset
from .pe import parse_pe
from .util import sha256_bytes, sha256_file, utc_now, write_json


def _checksum_offset(data: bytes | bytearray) -> int:
    """Locate the PE checksum field in a validated image buffer."""
    if len(data) < 0x40 or data[:2] != b"MZ":
        raise ContractError("input is not an MZ/PE image")
    pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
    if pe_offset + 4 + 20 + 68 > len(data) or data[pe_offset : pe_offset + 4] != b"PE\x00\x00":
        raise ContractError("input has an invalid PE header")
    return pe_offset + 4 + 20 + 64


def calculate_pe_checksum(data: bytes, checksum_offset: int) -> int:
    """Calculate the Windows PE checksum for an image buffer."""
    checksum = 0
    length = len(data)
    padded = data + (b"\x00" if length % 2 else b"")
    for offset in range(0, len(padded), 2):
        if checksum_offset <= offset < checksum_offset + 4:
            word = 0
        else:
            word = padded[offset] | (padded[offset + 1] << 8)
        checksum = (checksum + word) & 0xFFFFFFFF
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    checksum = (checksum & 0xFFFF) + (checksum >> 16)
    return (checksum + length) & 0xFFFFFFFF


def patch_pe_function(
    original_path: Path,
    candidate_path: Path,
    output_path: Path,
    *,
    function_rva: int,
    expected_original_sha256: str | None = None,
    expected_function_sha256: str | None = None,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Patch PE function."""
    original_path = original_path.resolve()
    candidate_path = candidate_path.resolve()
    if not original_path.is_file() or not candidate_path.is_file():
        raise ContractError("original PE and candidate code must exist")
    if expected_original_sha256 is not None and sha256_file(original_path) != expected_original_sha256:
        raise ContractError("original PE hash does not match expected_original_sha256")
    image = parse_pe(original_path)
    candidate = candidate_path.read_bytes()
    if not candidate:
        raise ContractError("candidate code is empty")
    file_offset = rva_to_file_offset(image, function_rva)
    payload = bytearray(original_path.read_bytes())
    if file_offset + len(candidate) > len(payload):
        raise ContractError("candidate patch exceeds PE file bounds")
    original_function = bytes(payload[file_offset : file_offset + len(candidate)])
    if expected_function_sha256 is not None and sha256_bytes(original_function) != expected_function_sha256:
        raise ContractError("original function bytes do not match expected_function_sha256")
    payload[file_offset : file_offset + len(candidate)] = candidate
    checksum_offset = _checksum_offset(payload)
    struct.pack_into("<I", payload, checksum_offset, 0)
    checksum = calculate_pe_checksum(bytes(payload), checksum_offset)
    struct.pack_into("<I", payload, checksum_offset, checksum)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(payload)
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "patch_image",
        "original": str(original_path),
        "original_sha256": sha256_file(original_path),
        "candidate": str(candidate_path),
        "candidate_sha256": sha256_file(candidate_path),
        "output": str(output_path.resolve()),
        "output_sha256": sha256_file(output_path),
        "function_rva": function_rva,
        "file_offset": file_offset,
        "patch_size": len(candidate),
        "original_function_sha256": sha256_bytes(original_function),
        "pe_checksum": checksum,
        "limitations": [
            "This backend replaces bytes in-place and cannot grow a function.",
            "Control-flow, unwind, relocation, and data references must already be valid for the patch location.",
        ],
    }
    if report_path is not None:
        write_json(report_path, report)
    return report

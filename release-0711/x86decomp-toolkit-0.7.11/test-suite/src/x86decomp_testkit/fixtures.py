"""Provide fixtures support for the standalone verification harness."""
from __future__ import annotations

import json
import struct
from pathlib import Path
from typing import Any


def write_json(path: Path, value: Any) -> Path:
    """Write JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def build_minimal_pe32(path: Path, code: bytes = b"\x55\x8b\xec\x31\xc0\x5d\xc3") -> Path:
    """Build minimal pe32."""
    pe_offset = 0x80
    optional_size = 224
    section_raw_offset = 0x200
    section_raw_size = 0x200
    data = bytearray(section_raw_offset + section_raw_size)
    data[0:2] = b"MZ"
    struct.pack_into("<I", data, 0x3C, pe_offset)
    data[pe_offset : pe_offset + 4] = b"PE\x00\x00"
    coff = pe_offset + 4
    struct.pack_into("<HHIIIHH", data, coff, 0x014C, 1, 0, 0, 0, optional_size, 0x0102)
    optional = coff + 20
    struct.pack_into("<H", data, optional + 0, 0x010B)
    struct.pack_into("<BB", data, optional + 2, 14, 0)
    struct.pack_into("<III", data, optional + 4, section_raw_size, 0, 0)
    struct.pack_into("<III", data, optional + 16, 0x1000, 0x1000, 0x2000)
    struct.pack_into("<I", data, optional + 28, 0x00400000)
    struct.pack_into("<II", data, optional + 32, 0x1000, 0x200)
    struct.pack_into("<HHHHHH", data, optional + 40, 6, 0, 0, 0, 6, 0)
    struct.pack_into("<I", data, optional + 52, 0)
    struct.pack_into("<II", data, optional + 56, 0x2000, 0x200)
    struct.pack_into("<I", data, optional + 64, 0)
    struct.pack_into("<HH", data, optional + 68, 3, 0x0140)
    struct.pack_into("<IIIIII", data, optional + 72, 0x100000, 0x1000, 0x100000, 0x1000, 0, 16)
    section = optional + optional_size
    data[section : section + 8] = b".text\x00\x00\x00"
    struct.pack_into("<IIIIIIHHI", data, section + 8, len(code), 0x1000, section_raw_size, section_raw_offset, 0, 0, 0, 0, 0x60000020)
    data[section_raw_offset : section_raw_offset + len(code)] = code
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def build_minimal_pe64(path: Path, code: bytes = b"\x31\xc0\xc3") -> Path:
    """Build minimal pe64."""
    pe_offset = 0x80
    optional_size = 240
    section_raw_offset = 0x200
    section_raw_size = 0x200
    data = bytearray(section_raw_offset + section_raw_size)
    data[0:2] = b"MZ"
    struct.pack_into("<I", data, 0x3C, pe_offset)
    data[pe_offset : pe_offset + 4] = b"PE\x00\x00"
    coff = pe_offset + 4
    struct.pack_into("<HHIIIHH", data, coff, 0x8664, 1, 0, 0, 0, optional_size, 0x0022)
    optional = coff + 20
    struct.pack_into("<H", data, optional, 0x020B)
    struct.pack_into("<BB", data, optional + 2, 14, 0)
    struct.pack_into("<III", data, optional + 4, section_raw_size, 0, 0)
    struct.pack_into("<II", data, optional + 16, 0x1000, 0x1000)
    struct.pack_into("<Q", data, optional + 24, 0x140000000)
    struct.pack_into("<II", data, optional + 32, 0x1000, 0x200)
    struct.pack_into("<HHHHHH", data, optional + 40, 6, 0, 0, 0, 6, 0)
    struct.pack_into("<I", data, optional + 52, 0)
    struct.pack_into("<II", data, optional + 56, 0x2000, 0x200)
    struct.pack_into("<I", data, optional + 64, 0)
    struct.pack_into("<HH", data, optional + 68, 3, 0x8160)
    struct.pack_into("<QQQQ", data, optional + 72, 0x100000, 0x1000, 0x100000, 0x1000)
    struct.pack_into("<II", data, optional + 104, 0, 16)
    section = optional + optional_size
    data[section : section + 8] = b".text\x00\x00\x00"
    struct.pack_into("<IIIIIIHHI", data, section + 8, len(code), 0x1000, section_raw_size, section_raw_offset, 0, 0, 0, 0, 0x60000020)
    data[section_raw_offset : section_raw_offset + len(code)] = code
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def create_common_fixtures(root: Path) -> dict[str, Path]:
    """Create common fixtures."""
    root.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    paths["pe32"] = build_minimal_pe32(root / "minimal32.exe")
    paths["pe64"] = build_minimal_pe64(root / "minimal64.exe")
    paths["code_equal_a"] = root / "target.bin"
    paths["code_equal_b"] = root / "candidate.bin"
    paths["code_different"] = root / "different.bin"
    paths["code_equal_a"].write_bytes(b"\xb8\x2a\x00\x00\x00\xc3")
    paths["code_equal_b"].write_bytes(b"\xb8\x2a\x00\x00\x00\xc3")
    paths["code_different"].write_bytes(b"\xb8\x2b\x00\x00\x00\xc3")
    paths["abi"] = write_json(
        root / "abi.json",
        {
            "architecture": "x86",
            "convention": "cdecl",
            "stack_argument_bytes": 0,
            "callee_stack_cleanup": 0,
            "variadic": False,
            "this_register": None,
            "register_arguments": [],
            "return_registers": ["eax"],
            "structure_return": False,
            "floating_point": "none",
        },
    )
    paths["dynamic_harness"] = write_json(
        root / "dynamic-harness.json",
        {
            "architecture": "x86",
            "observe_registers": ["eax", "esp", "eflags"],
            "max_instructions": 100,
            "timeout_ms": 1000,
        },
    )
    paths["drcov"] = root / "sample.drcov.log"
    paths["drcov"].write_text(
        "DRCOV VERSION: 2\n"
        "DRCOV FLAVOR: drcov\n"
        "Module Table: version 2, count 1\n"
        "Columns: id, base, end, entry, checksum, timestamp, path\n"
        "0, 0x1000, 0x2000, 0x1000, 0x0, 0x0, /tmp/sample\n"
        "BB Table: 1 bbs\n"
        "module[  0]: 0x10, 5\n",
        encoding="utf-8",
    )
    return paths

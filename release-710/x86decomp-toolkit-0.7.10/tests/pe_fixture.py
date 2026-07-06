"""Verify the current toolkit behavior covered by `tests/pe_fixture.py`."""
from __future__ import annotations

import struct
from pathlib import Path


def build_minimal_pe32(path: Path, code: bytes = b"\x55\x8b\xec\x31\xc0\x5d\xc3") -> Path:
    """Build minimal pe32 for the current toolkit workflow."""
    pe_offset = 0x80
    optional_size = 224
    section_raw_offset = 0x200
    section_raw_size = 0x200
    data = bytearray(section_raw_offset + section_raw_size)
    data[0:2] = b"MZ"
    struct.pack_into("<I", data, 0x3C, pe_offset)
    data[pe_offset : pe_offset + 4] = b"PE\x00\x00"
    coff = pe_offset + 4
    struct.pack_into(
        "<HHIIIHH",
        data,
        coff,
        0x014C,
        1,
        0,
        0,
        0,
        optional_size,
        0x0102,
    )
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
    struct.pack_into(
        "<IIIIIIHHI",
        data,
        section + 8,
        len(code),
        0x1000,
        section_raw_size,
        section_raw_offset,
        0,
        0,
        0,
        0,
        0x60000020,
    )
    data[section_raw_offset : section_raw_offset + len(code)] = code
    path.write_bytes(data)
    return path


def build_minimal_pe64(path: Path, code: bytes = b"\x31\xc0\xc3") -> Path:
    """Build minimal pe64 for the current toolkit workflow."""
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
    path.write_bytes(data)
    return path

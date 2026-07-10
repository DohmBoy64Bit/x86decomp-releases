---
title: x86decomp.binary_reader
description: Module reference for x86decomp.binary_reader.
---

# `x86decomp.binary_reader`

- Area: `toolkit`
- Source path: `src/x86decomp/binary_reader.py`
- SHA-256: `484e3667fb7a5301501d453e8393264f10d8bc9f2d76810405cd16038faa04e4`
- Size: `2867` bytes
- Lines: `62`

## Module docstring

Shared bounded binary-reading primitives for PE and COFF parsers.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `BinaryReader` | 10 | Read little-endian binary structures while enforcing file bounds. |
| function | `__init__` | 13 | Store immutable input bytes for bounded reads. |
| function | `require` | 17 | Raise ``FormatError`` when a requested byte range is outside the file. |
| function | `unpack` | 24 | Unpack a structure after validating that the entire range exists. |
| function | `u16` | 30 | Read an unsigned little-endian 16-bit integer. |
| function | `u32` | 34 | Read an unsigned little-endian 32-bit integer. |
| function | `u64` | 38 | Read an unsigned little-endian 64-bit integer. |
| function | `c_string` | 42 | Read a bounded NUL-terminated UTF-8 string. |
| function | `optional_u16` | 51 | Read a relative 16-bit field when it is present in a bounded record. |
| function | `optional_u32` | 55 | Read a relative 32-bit field when it is present in a bounded record. |
| function | `optional_u64` | 59 | Read a relative 64-bit field when it is present in a bounded record. |

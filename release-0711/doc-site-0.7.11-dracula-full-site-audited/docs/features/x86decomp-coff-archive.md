---
title: x86decomp.coff_archive
description: Module reference for x86decomp.coff_archive.
---

# `x86decomp.coff_archive`

- Area: `toolkit`
- Source path: `src/x86decomp/coff_archive.py`
- SHA-256: `334fc0ec09fc70cb1ec34654cd73ae4e5ba14650fb6afef97791f9cf088459d1`
- Size: `13325` bytes
- Lines: `335`

## Module docstring

Bounded Microsoft/Unix COFF archive (``.lib``/``.a``) inspection.

The archive container format is shared with ``ar``. Microsoft libraries additionally
use linker members and import-object records. This module inventories members, resolves
long names, parses linker symbol indexes when structurally valid, recognizes import
objects, and invokes the normal COFF parser for embedded object members.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `ArchiveMember` | 27 | Store validated archive member fields used by toolkit reports and adapters. |
| function | `to_dict` | 43 | Return a serializable dictionary representation. |
| class | `CoffArchive` | 66 | Store validated coff archive fields used by toolkit reports and adapters. |
| function | `to_dict` | 73 | Return a serializable dictionary representation. |
| function | `_decimal` | 86 | Support decimal processing for internal toolkit callers. |
| function | `_octal` | 97 | Support octal processing for internal toolkit callers. |
| function | `_long_name` | 108 | Support long name processing for internal toolkit callers. |
| function | `_parse_import_object` | 117 | Support parse import object processing for internal toolkit callers. |
| function | `_cstring_sequence` | 155 | Support cstring sequence processing for internal toolkit callers. |
| function | `_first_linker_symbols` | 170 | Support first linker symbols processing for internal toolkit callers. |
| function | `_second_linker_symbols` | 185 | Support second linker symbols processing for internal toolkit callers. |
| function | `parse_coff_archive_bytes` | 213 | Parse coff archive bytes for the current toolkit workflow. |
| function | `parse_coff_archive` | 326 | Parse coff archive for the current toolkit workflow. |

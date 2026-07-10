---
title: x86decomp.pe32
description: Module reference for x86decomp.pe32.
---

# `x86decomp.pe32`

- Area: `toolkit`
- Source path: `src/x86decomp/pe32.py`
- SHA-256: `1487c4fa4c92d7b161f89beac59c79fab7672439806825ed76010f63fd598837`
- Size: `38285` bytes
- Lines: `959`

## Module docstring

Strict, dependency-free parser for native x86 PE32 images.

The parser intentionally supports the first toolkit scope only: little-endian
Windows PE32 images for IMAGE_FILE_MACHINE_I386. It never executes the input.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `DataDirectory` | 43 | Store validated data directory fields used by toolkit reports and adapters. |
| function | `to_dict` | 49 | Return a serializable dictionary representation. |
| class | `Section` | 55 | Store validated section fields used by toolkit reports and adapters. |
| function | `mapped_size` | 66 | Execute the mapped size operation for the current toolkit workflow. |
| function | `to_dict` | 70 | Return a serializable dictionary representation. |
| class | `ImportSymbol` | 86 | Store validated import symbol fields used by toolkit reports and adapters. |
| function | `to_dict` | 94 | Return a serializable dictionary representation. |
| class | `ImportLibrary` | 106 | Store validated import library fields used by toolkit reports and adapters. |
| function | `to_dict` | 111 | Return a serializable dictionary representation. |
| class | `ExportSymbol` | 117 | Store validated export symbol fields used by toolkit reports and adapters. |
| function | `to_dict` | 124 | Return a serializable dictionary representation. |
| class | `BaseRelocation` | 136 | Store validated base relocation fields used by toolkit reports and adapters. |
| function | `to_dict` | 141 | Return a serializable dictionary representation. |
| class | `DebugRecord` | 147 | Store validated debug record fields used by toolkit reports and adapters. |
| function | `to_dict` | 158 | Return a serializable dictionary representation. |
| class | `TLSInfo` | 173 | Store validated t l s info fields used by toolkit reports and adapters. |
| function | `to_dict` | 183 | Return a serializable dictionary representation. |
| class | `ResourceLeaf` | 199 | Store validated resource leaf fields used by toolkit reports and adapters. |
| function | `to_dict` | 207 | Return a serializable dictionary representation. |
| class | `DelayImportLibrary` | 220 | Store validated delay import library fields used by toolkit reports and adapters. |
| function | `to_dict` | 227 | Return a serializable dictionary representation. |
| class | `LoadConfigInfo` | 238 | Store validated load config info fields used by toolkit reports and adapters. |
| function | `to_dict` | 255 | Return a serializable dictionary representation. |
| class | `PE32Image` | 276 | Store validated p e32 image fields used by toolkit reports and adapters. |
| function | `entry_va` | 305 | Execute the entry va operation for the current toolkit workflow. |
| function | `to_dict` | 309 | Return a serializable dictionary representation. |
| function | `_rva_to_offset` | 351 | Support rva to offset processing for internal toolkit callers. |
| function | `_directory` | 373 | Support directory processing for internal toolkit callers. |
| function | `_parse_imports` | 381 | Support parse imports processing for internal toolkit callers. |
| function | `_parse_exports` | 454 | Support parse exports processing for internal toolkit callers. |
| function | `_parse_relocations` | 521 | Support parse relocations processing for internal toolkit callers. |
| function | `_parse_debug_records` | 555 | Support parse debug records processing for internal toolkit callers. |
| function | `_parse_tls` | 617 | Support parse tls processing for internal toolkit callers. |
| function | `_parse_resources` | 664 | Support parse resources processing for internal toolkit callers. |
| function | `read_name` | 680 | Read name for the current toolkit workflow. |
| function | `walk` | 690 | Execute the walk operation for the current toolkit workflow. |
| function | `_parse_delay_imports` | 732 | Support parse delay imports processing for internal toolkit callers. |
| function | `to_rva` | 753 | Execute the to rva operation for the current toolkit workflow. |
| function | `_parse_load_config` | 793 | Support parse load config processing for internal toolkit callers. |
| function | `parse_pe32` | 826 | Parse pe32 for the current toolkit workflow. |

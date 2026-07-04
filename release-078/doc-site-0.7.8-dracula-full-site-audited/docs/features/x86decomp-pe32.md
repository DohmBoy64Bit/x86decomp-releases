---
title: x86decomp.pe32
description: Source module reference for x86decomp.pe32.
---

# `x86decomp.pe32`

**Source path:** `src/x86decomp/pe32.py`  
**Documented symbols:** 50

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `DataDirectory` | class | 42 | 48 | — |
| `to_dict` | function | 47 | 48 | — |
| `Section` | class | 52 | 76 | — |
| `mapped_size` | function | 62 | 63 | — |
| `to_dict` | function | 65 | 76 | — |
| `ImportSymbol` | class | 80 | 94 | — |
| `to_dict` | function | 87 | 94 | — |
| `ImportLibrary` | class | 98 | 103 | — |
| `to_dict` | function | 102 | 103 | — |
| `ExportSymbol` | class | 107 | 120 | — |
| `to_dict` | function | 113 | 120 | — |
| `BaseRelocation` | class | 124 | 129 | — |
| `to_dict` | function | 128 | 129 | — |
| `DebugRecord` | class | 133 | 153 | — |
| `to_dict` | function | 143 | 153 | — |
| `TLSInfo` | class | 157 | 175 | — |
| `to_dict` | function | 166 | 175 | — |
| `ResourceLeaf` | class | 181 | 196 | — |
| `to_dict` | function | 188 | 196 | — |
| `DelayImportLibrary` | class | 200 | 212 | — |
| `to_dict` | function | 206 | 212 | — |
| `LoadConfigInfo` | class | 216 | 248 | — |
| `to_dict` | function | 232 | 248 | — |
| `PE32Image` | class | 252 | 319 | — |
| `entry_va` | function | 280 | 281 | — |
| `to_dict` | function | 283 | 319 | — |
| `_Reader` | class | 322 | 352 | — |
| `__init__` | function | 323 | 324 | — |
| `require` | function | 326 | 330 | — |
| `unpack` | function | 332 | 335 | — |
| `u16` | function | 337 | 338 | — |
| `u32` | function | 340 | 341 | — |
| `u64` | function | 343 | 344 | — |
| `c_string` | function | 346 | 352 | — |
| `_rva_to_offset` | function | 355 | 373 | — |
| `_directory` | function | 376 | 380 | — |
| `_parse_imports` | function | 383 | 452 | — |
| `_parse_exports` | function | 455 | 518 | — |
| `_parse_relocations` | function | 521 | 551 | — |
| `_parse_debug_records` | function | 554 | 612 | — |
| `_parse_tls` | function | 615 | 657 | — |
| `_parse_resources` | function | 661 | 723 | — |
| `read_name` | function | 676 | 683 | — |
| `walk` | function | 685 | 720 | — |
| `_parse_delay_imports` | function | 726 | 782 | — |
| `to_rva` | function | 746 | 753 | — |
| `_parse_load_config` | function | 785 | 821 | — |
| `u16_at` | function | 800 | 801 | — |
| `u32_at` | function | 803 | 804 | — |
| `parse_pe32` | function | 823 | 954 | — |

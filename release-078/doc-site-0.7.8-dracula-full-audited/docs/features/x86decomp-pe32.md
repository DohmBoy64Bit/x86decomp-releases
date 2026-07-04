---
title: x86decomp.pe32
description: Source module reference for x86decomp.pe32.
---

# `x86decomp.pe32`

**Source path:** `src/x86decomp/pe32.py`  
**SHA-256:** `746651d78b0b8401565dd22e99f73c8c902b13400fd80094d4675ab52c8c4be5`  
**Documented symbols:** 50

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `DataDirectory` | class | 42 | 48 | no docstring declared |
| `to_dict` | function | 47 | 48 | no docstring declared |
| `Section` | class | 52 | 76 | no docstring declared |
| `mapped_size` | function | 62 | 63 | no docstring declared |
| `to_dict` | function | 65 | 76 | no docstring declared |
| `ImportSymbol` | class | 80 | 94 | no docstring declared |
| `to_dict` | function | 87 | 94 | no docstring declared |
| `ImportLibrary` | class | 98 | 103 | no docstring declared |
| `to_dict` | function | 102 | 103 | no docstring declared |
| `ExportSymbol` | class | 107 | 120 | no docstring declared |
| `to_dict` | function | 113 | 120 | no docstring declared |
| `BaseRelocation` | class | 124 | 129 | no docstring declared |
| `to_dict` | function | 128 | 129 | no docstring declared |
| `DebugRecord` | class | 133 | 153 | no docstring declared |
| `to_dict` | function | 143 | 153 | no docstring declared |
| `TLSInfo` | class | 157 | 175 | no docstring declared |
| `to_dict` | function | 166 | 175 | no docstring declared |
| `ResourceLeaf` | class | 181 | 196 | no docstring declared |
| `to_dict` | function | 188 | 196 | no docstring declared |
| `DelayImportLibrary` | class | 200 | 212 | no docstring declared |
| `to_dict` | function | 206 | 212 | no docstring declared |
| `LoadConfigInfo` | class | 216 | 248 | no docstring declared |
| `to_dict` | function | 232 | 248 | no docstring declared |
| `PE32Image` | class | 252 | 319 | no docstring declared |
| `entry_va` | function | 280 | 281 | no docstring declared |
| `to_dict` | function | 283 | 319 | no docstring declared |
| `_Reader` | class | 322 | 352 | no docstring declared |
| `__init__` | function | 323 | 324 | no docstring declared |
| `require` | function | 326 | 330 | no docstring declared |
| `unpack` | function | 332 | 335 | no docstring declared |
| `u16` | function | 337 | 338 | no docstring declared |
| `u32` | function | 340 | 341 | no docstring declared |
| `u64` | function | 343 | 344 | no docstring declared |
| `c_string` | function | 346 | 352 | no docstring declared |
| `_rva_to_offset` | function | 355 | 373 | no docstring declared |
| `_directory` | function | 376 | 380 | no docstring declared |
| `_parse_imports` | function | 383 | 452 | no docstring declared |
| `_parse_exports` | function | 455 | 518 | no docstring declared |
| `_parse_relocations` | function | 521 | 551 | no docstring declared |
| `_parse_debug_records` | function | 554 | 612 | no docstring declared |
| `_parse_tls` | function | 615 | 657 | no docstring declared |
| `_parse_resources` | function | 661 | 723 | no docstring declared |
| `read_name` | function | 676 | 683 | no docstring declared |
| `walk` | function | 685 | 720 | no docstring declared |
| `_parse_delay_imports` | function | 726 | 782 | no docstring declared |
| `to_rva` | function | 746 | 753 | no docstring declared |
| `_parse_load_config` | function | 785 | 821 | no docstring declared |
| `u16_at` | function | 800 | 801 | no docstring declared |
| `u32_at` | function | 803 | 804 | no docstring declared |
| `parse_pe32` | function | 823 | 954 | no docstring declared |

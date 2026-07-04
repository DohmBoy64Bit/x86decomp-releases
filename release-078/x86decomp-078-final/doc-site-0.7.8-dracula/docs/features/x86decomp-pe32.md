---
title: x86decomp.pe32
description: Source module reference for x86decomp.pe32.
---

# `x86decomp.pe32`

**Source path:** `src/x86decomp/pe32.py`  
**SHA-256:** `746651d78b0b8401565dd22e99f73c8c902b13400fd80094d4675ab52c8c4be5`

| Symbol | Kind | Line | Body lines |
| --- | --- | ---: | --- |
| `DataDirectory.to_dict` | method | 47 | 48 |
| `Section.mapped_size` | method | 62 | 63 |
| `Section.to_dict` | method | 65 | 66 |
| `ImportSymbol.to_dict` | method | 87 | 88 |
| `ImportLibrary.to_dict` | method | 102 | 103 |
| `ExportSymbol.to_dict` | method | 113 | 114 |
| `BaseRelocation.to_dict` | method | 128 | 129 |
| `DebugRecord.to_dict` | method | 143 | 144 |
| `TLSInfo.to_dict` | method | 166 | 167 |
| `ResourceLeaf.to_dict` | method | 188 | 189 |
| `DelayImportLibrary.to_dict` | method | 206 | 207 |
| `LoadConfigInfo.to_dict` | method | 232 | 233 |
| `PE32Image.entry_va` | method | 280 | 281 |
| `PE32Image.to_dict` | method | 283 | 284 |
| `_Reader.__init__` | method | 323 | 324 |
| `_Reader.require` | method | 326 | 327 |
| `_Reader.unpack` | method | 332 | 333, 334, 335 |
| `_Reader.u16` | method | 337 | 338 |
| `_Reader.u32` | method | 340 | 341 |
| `_Reader.u64` | method | 343 | 344 |
| `_Reader.c_string` | method | 346 | 347, 348, 349, 350, 352 |
| `_rva_to_offset` | function | 355 | 356, 360, 373 |
| `_directory` | function | 376 | 377, 380 |
| `_parse_imports` | function | 383 | 389, 390, 392, 395, 396, 397, 452 |
| `_parse_exports` | function | 455 | 461, 462, 464, 465, 478, 480, 483, 484, 487, 488, 498, 499… |
| `_parse_relocations` | function | 521 | 527, 528, 530, 531, 532, 533, 551 |
| `_parse_debug_records` | function | 554 | 560, 561, 563, 565, 566, 567, 612 |
| `_parse_tls` | function | 615 | 622, 623, 625, 626, 634, 635, 649 |
| `_parse_resources` | function | 661 | 667, 668, 670, 671, 672, 673, 674, 676, 685, 722, 723 |
| `_parse_delay_imports` | function | 726 | 733, 734, 736, 737, 738, 739, 782 |
| `_parse_load_config` | function | 785 | 791, 792, 794, 795, 796, 797, 800, 803, 806 |
| `parse_pe32` | function | 823 | 824, 825, 827, 828, 829, 830, 832, 833, 834, 836, 837, 846… |

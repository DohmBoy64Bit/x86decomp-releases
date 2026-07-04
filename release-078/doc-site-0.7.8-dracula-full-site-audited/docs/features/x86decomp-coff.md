---
title: x86decomp.coff
description: Source module reference for x86decomp.coff.
---

# `x86decomp.coff`

**Source path:** `src/x86decomp/coff.py`  
**Documented symbols:** 68

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `relocation_name` | function | 127 | 129 | — |
| `relocation_width` | function | 132 | 134 | — |
| `relocation_is_pc_relative` | function | 137 | 140 | — |
| `CoffRelocation` | class | 144 | 165 | — |
| `width` | function | 151 | 152 | — |
| `to_dict` | function | 154 | 165 | — |
| `SectionDefinitionAux` | class | 169 | 192 | — |
| `selection_name` | function | 178 | 179 | — |
| `to_dict` | function | 181 | 192 | — |
| `FunctionDefinitionAux` | class | 196 | 209 | — |
| `to_dict` | function | 202 | 209 | — |
| `WeakExternalAux` | class | 213 | 224 | — |
| `to_dict` | function | 217 | 224 | — |
| `FileAux` | class | 228 | 232 | — |
| `to_dict` | function | 231 | 232 | — |
| `RawAux` | class | 236 | 240 | — |
| `to_dict` | function | 239 | 240 | — |
| `CoffSection` | class | 247 | 305 | — |
| `is_comdat` | function | 263 | 264 | — |
| `comdat_selection_name` | function | 267 | 268 | — |
| `alignment_power` | function | 271 | 277 | — |
| `alignment` | function | 280 | 282 | — |
| `to_dict` | function | 284 | 305 | — |
| `CoffSymbol` | class | 309 | 357 | — |
| `is_function` | function | 320 | 323 | — |
| `section_definition` | function | 326 | 330 | — |
| `function_definition` | function | 333 | 337 | — |
| `weak_external` | function | 340 | 344 | — |
| `to_dict` | function | 346 | 357 | — |
| `CoffObject` | class | 361 | 408 | — |
| `architecture` | function | 373 | 378 | — |
| `section` | function | 380 | 383 | — |
| `find_symbols` | function | 385 | 389 | — |
| `symbol_by_index` | function | 391 | 392 | — |
| `to_dict` | function | 394 | 408 | — |
| `ExtractedSymbol` | class | 412 | 428 | — |
| `to_dict` | function | 420 | 428 | — |
| `ComdatCandidate` | class | 432 | 455 | — |
| `to_dict` | function | 443 | 455 | — |
| `ComdatResolution` | class | 459 | 475 | — |
| `valid` | function | 465 | 466 | — |
| `to_dict` | function | 468 | 475 | — |
| `SyntheticSymbolSpec` | class | 479 | 485 | — |
| `SyntheticSectionSpec` | class | 489 | 497 | — |
| `_Reader` | class | 500 | 513 | — |
| `__init__` | function | 501 | 502 | — |
| `require` | function | 504 | 508 | — |
| `unpack` | function | 510 | 513 | — |
| `_read_string_table` | function | 516 | 527 | — |
| `_string_at` | function | 530 | 536 | — |
| `_decode_symbol_name` | function | 539 | 543 | — |
| `_decode_section_name` | function | 546 | 550 | — |
| `_parse_header` | function | 553 | 604 | Return variant, machine, sections, timestamp, symptr, symcount, |
| `_parse_auxiliary_records` | function | 607 | 662 | — |
| `_read_addend` | function | 665 | 668 | — |
| `parse_coff_bytes` | function | 671 | 866 | — |
| `parse_coff` | function | 869 | 873 | — |
| `extract_symbol` | function | 876 | 928 | — |
| `collect_comdat_candidates` | function | 931 | 955 | — |
| `resolve_comdats` | function | 958 | 1056 | Resolve COMDAT groups using PE/COFF selection semantics. |
| `_encode_name` | function | 1059 | 1065 | — |
| `_section_aux_bytes` | function | 1068 | 1081 | — |
| `build_synthetic_coff_object` | function | 1084 | 1198 | Build a deterministic classic COFF object with multiple sections. |
| `synthetic_symbol_indices` | function | 1201 | 1209 | — |
| `build_synthetic_coff` | function | 1212 | 1249 | Backward-compatible one-section synthetic COFF builder. |
| `build_comdat_coff` | function | 1252 | 1314 | — |
| `write_synthetic_coff` | function | 1317 | 1331 | — |
| `write_synthetic_coff_object` | function | 1334 | 1347 | — |

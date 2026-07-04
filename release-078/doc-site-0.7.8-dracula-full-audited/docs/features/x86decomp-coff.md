---
title: x86decomp.coff
description: Source module reference for x86decomp.coff.
---

# `x86decomp.coff`

**Source path:** `src/x86decomp/coff.py`  
**SHA-256:** `f6900af73b991d2ed380250c78d4a228ff6b10f45bd4bcf04fb449c45f13d28e`  
**Documented symbols:** 68

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `relocation_name` | function | 127 | 129 | no docstring declared |
| `relocation_width` | function | 132 | 134 | no docstring declared |
| `relocation_is_pc_relative` | function | 137 | 140 | no docstring declared |
| `CoffRelocation` | class | 144 | 165 | no docstring declared |
| `width` | function | 151 | 152 | no docstring declared |
| `to_dict` | function | 154 | 165 | no docstring declared |
| `SectionDefinitionAux` | class | 169 | 192 | no docstring declared |
| `selection_name` | function | 178 | 179 | no docstring declared |
| `to_dict` | function | 181 | 192 | no docstring declared |
| `FunctionDefinitionAux` | class | 196 | 209 | no docstring declared |
| `to_dict` | function | 202 | 209 | no docstring declared |
| `WeakExternalAux` | class | 213 | 224 | no docstring declared |
| `to_dict` | function | 217 | 224 | no docstring declared |
| `FileAux` | class | 228 | 232 | no docstring declared |
| `to_dict` | function | 231 | 232 | no docstring declared |
| `RawAux` | class | 236 | 240 | no docstring declared |
| `to_dict` | function | 239 | 240 | no docstring declared |
| `CoffSection` | class | 247 | 305 | no docstring declared |
| `is_comdat` | function | 263 | 264 | no docstring declared |
| `comdat_selection_name` | function | 267 | 268 | no docstring declared |
| `alignment_power` | function | 271 | 277 | no docstring declared |
| `alignment` | function | 280 | 282 | no docstring declared |
| `to_dict` | function | 284 | 305 | no docstring declared |
| `CoffSymbol` | class | 309 | 357 | no docstring declared |
| `is_function` | function | 320 | 323 | no docstring declared |
| `section_definition` | function | 326 | 330 | no docstring declared |
| `function_definition` | function | 333 | 337 | no docstring declared |
| `weak_external` | function | 340 | 344 | no docstring declared |
| `to_dict` | function | 346 | 357 | no docstring declared |
| `CoffObject` | class | 361 | 408 | no docstring declared |
| `architecture` | function | 373 | 378 | no docstring declared |
| `section` | function | 380 | 383 | no docstring declared |
| `find_symbols` | function | 385 | 389 | no docstring declared |
| `symbol_by_index` | function | 391 | 392 | no docstring declared |
| `to_dict` | function | 394 | 408 | no docstring declared |
| `ExtractedSymbol` | class | 412 | 428 | no docstring declared |
| `to_dict` | function | 420 | 428 | no docstring declared |
| `ComdatCandidate` | class | 432 | 455 | no docstring declared |
| `to_dict` | function | 443 | 455 | no docstring declared |
| `ComdatResolution` | class | 459 | 475 | no docstring declared |
| `valid` | function | 465 | 466 | no docstring declared |
| `to_dict` | function | 468 | 475 | no docstring declared |
| `SyntheticSymbolSpec` | class | 479 | 485 | no docstring declared |
| `SyntheticSectionSpec` | class | 489 | 497 | no docstring declared |
| `_Reader` | class | 500 | 513 | no docstring declared |
| `__init__` | function | 501 | 502 | no docstring declared |
| `require` | function | 504 | 508 | no docstring declared |
| `unpack` | function | 510 | 513 | no docstring declared |
| `_read_string_table` | function | 516 | 527 | no docstring declared |
| `_string_at` | function | 530 | 536 | no docstring declared |
| `_decode_symbol_name` | function | 539 | 543 | no docstring declared |
| `_decode_section_name` | function | 546 | 550 | no docstring declared |
| `_parse_header` | function | 553 | 604 | Return variant, machine, sections, timestamp, symptr, symcount, |
| `_parse_auxiliary_records` | function | 607 | 662 | no docstring declared |
| `_read_addend` | function | 665 | 668 | no docstring declared |
| `parse_coff_bytes` | function | 671 | 866 | no docstring declared |
| `parse_coff` | function | 869 | 873 | no docstring declared |
| `extract_symbol` | function | 876 | 928 | no docstring declared |
| `collect_comdat_candidates` | function | 931 | 955 | no docstring declared |
| `resolve_comdats` | function | 958 | 1056 | Resolve COMDAT groups using PE/COFF selection semantics. |
| `_encode_name` | function | 1059 | 1065 | no docstring declared |
| `_section_aux_bytes` | function | 1068 | 1081 | no docstring declared |
| `build_synthetic_coff_object` | function | 1084 | 1198 | Build a deterministic classic COFF object with multiple sections. |
| `synthetic_symbol_indices` | function | 1201 | 1209 | no docstring declared |
| `build_synthetic_coff` | function | 1212 | 1249 | Backward-compatible one-section synthetic COFF builder. |
| `build_comdat_coff` | function | 1252 | 1314 | no docstring declared |
| `write_synthetic_coff` | function | 1317 | 1331 | no docstring declared |
| `write_synthetic_coff_object` | function | 1334 | 1347 | no docstring declared |

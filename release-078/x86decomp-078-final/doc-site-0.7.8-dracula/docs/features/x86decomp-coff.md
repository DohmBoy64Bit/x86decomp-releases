---
title: x86decomp.coff
description: Source module reference for x86decomp.coff.
---

# `x86decomp.coff`

**Source path:** `src/x86decomp/coff.py`  
**SHA-256:** `f6900af73b991d2ed380250c78d4a228ff6b10f45bd4bcf04fb449c45f13d28e`

| Symbol | Kind | Line | Body lines |
| --- | --- | ---: | --- |
| `relocation_name` | function | 127 | 128, 129 |
| `relocation_width` | function | 132 | 133, 134 |
| `relocation_is_pc_relative` | function | 137 | 138, 140 |
| `CoffRelocation.width` | method | 151 | 152 |
| `CoffRelocation.to_dict` | method | 154 | 155 |
| `SectionDefinitionAux.selection_name` | method | 178 | 179 |
| `SectionDefinitionAux.to_dict` | method | 181 | 182 |
| `FunctionDefinitionAux.to_dict` | method | 202 | 203 |
| `WeakExternalAux.to_dict` | method | 217 | 218, 219 |
| `FileAux.to_dict` | method | 231 | 232 |
| `RawAux.to_dict` | method | 239 | 240 |
| `CoffSection.is_comdat` | method | 263 | 264 |
| `CoffSection.comdat_selection_name` | method | 267 | 268 |
| `CoffSection.alignment_power` | method | 271 | 272, 273, 275, 277 |
| `CoffSection.alignment` | method | 280 | 281, 282 |
| `CoffSection.to_dict` | method | 284 | 285 |
| `CoffSymbol.is_function` | method | 320 | 321 |
| `CoffSymbol.section_definition` | method | 326 | 327 |
| `CoffSymbol.function_definition` | method | 333 | 334 |
| `CoffSymbol.weak_external` | method | 340 | 341 |
| `CoffSymbol.to_dict` | method | 346 | 347 |
| `CoffObject.architecture` | method | 373 | 374, 376, 378 |
| `CoffObject.section` | method | 380 | 381, 383 |
| `CoffObject.find_symbols` | method | 385 | 386, 387, 389 |
| `CoffObject.symbol_by_index` | method | 391 | 392 |
| `CoffObject.to_dict` | method | 394 | 395 |
| `ExtractedSymbol.to_dict` | method | 420 | 421 |
| `ComdatCandidate.to_dict` | method | 443 | 444 |
| `ComdatResolution.valid` | method | 465 | 466 |
| `ComdatResolution.to_dict` | method | 468 | 469 |
| `_Reader.__init__` | method | 501 | 502 |
| `_Reader.require` | method | 504 | 505 |
| `_Reader.unpack` | method | 510 | 511, 512, 513 |
| `_read_string_table` | function | 516 | 519, 520, 522, 523, 524, 526, 527 |
| `_string_at` | function | 530 | 531, 533, 534, 536 |
| `_decode_symbol_name` | function | 539 | 540, 543 |
| `_decode_section_name` | function | 546 | 547, 548, 550 |
| `_parse_header` | function | 553 | 557, 558, 559, 589, 592, 594 |
| `_parse_auxiliary_records` | function | 607 | 616, 618, 621, 622, 645, 651, 662 |
| `_read_addend` | function | 665 | 666, 668 |
| `parse_coff_bytes` | function | 671 | 672, 673, 684, 686, 688, 689, 691, 697, 698, 748, 749, 750… |
| `parse_coff` | function | 869 | 870, 871, 873 |
| `extract_symbol` | function | 876 | 877, 878, 881, 889, 890, 891, 893, 908, 910, 921 |
| `collect_comdat_candidates` | function | 931 | 932, 933, 955 |
| `resolve_comdats` | function | 958 | 965, 966, 967, 968, 973, 974, 975, 976, 978, 1045, 1052 |
| `_encode_name` | function | 1059 | 1060, 1061, 1063, 1064, 1065 |
| `_section_aux_bytes` | function | 1068 | 1071 |
| `build_synthetic_coff_object` | function | 1084 | 1097, 1099, 1101, 1103, 1114, 1124, 1125, 1126, 1128, 1129, 1130, 1131… |
| `synthetic_symbol_indices` | function | 1201 | 1202, 1203, 1204, 1209 |
| `build_synthetic_coff` | function | 1212 | 1221, 1223, 1225, 1226, 1229 |
| `build_comdat_coff` | function | 1252 | 1264, 1266, 1267, 1275, 1285 |
| `write_synthetic_coff` | function | 1317 | 1325, 1328, 1329, 1330, 1331 |
| `write_synthetic_coff_object` | function | 1334 | 1342, 1345, 1346, 1347 |

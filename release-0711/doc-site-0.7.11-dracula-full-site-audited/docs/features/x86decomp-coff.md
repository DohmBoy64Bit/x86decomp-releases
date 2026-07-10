---
title: x86decomp.coff
description: Module reference for x86decomp.coff.
---

# `x86decomp.coff`

- Area: `toolkit`
- Source path: `src/x86decomp/coff.py`
- SHA-256: `4630e57a2d64ffb3d9961e044437d5fe5f0bb4811a2c9748515baf59b167f798`
- Size: `51950` bytes
- Lines: `1395`

## Module docstring

Strict COFF object parsing, COMDAT resolution, and deterministic synthesis.

The implementation covers classic Microsoft COFF and ``ANON_OBJECT_HEADER_BIGOBJ``
objects for IMAGE_FILE_MACHINE_I386 and IMAGE_FILE_MACHINE_AMD64.  It preserves
auxiliary symbol records, section-definition COMDAT metadata, weak externals,
function definitions, relocation-overflow records, and enough linker semantics
to reconstruct deterministic object groups for matching-decompilation projects.

It intentionally does not pretend that a linked PE still contains every original
COFF relocation.  This module operates on actual object files or explicitly
reconstructed synthetic objects.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `relocation_name` | 128 | Execute the relocation name operation for the current toolkit workflow. |
| function | `relocation_width` | 134 | Execute the relocation width operation for the current toolkit workflow. |
| function | `relocation_is_pc_relative` | 140 | Execute the relocation is pc relative operation for the current toolkit workflow. |
| class | `CoffRelocation` | 148 | Store validated coff relocation fields used by toolkit reports and adapters. |
| function | `width` | 156 | Execute the width operation for the current toolkit workflow. |
| function | `to_dict` | 160 | Return a serializable dictionary representation. |
| class | `SectionDefinitionAux` | 176 | Store validated section definition aux fields used by toolkit reports and adapters. |
| function | `selection_name` | 186 | Select ion name for the current toolkit workflow. |
| function | `to_dict` | 190 | Return a serializable dictionary representation. |
| class | `FunctionDefinitionAux` | 206 | Store validated function definition aux fields used by toolkit reports and adapters. |
| function | `to_dict` | 213 | Return a serializable dictionary representation. |
| class | `WeakExternalAux` | 225 | Store validated weak external aux fields used by toolkit reports and adapters. |
| function | `to_dict` | 230 | Return a serializable dictionary representation. |
| class | `FileAux` | 242 | Store validated file aux fields used by toolkit reports and adapters. |
| function | `to_dict` | 246 | Return a serializable dictionary representation. |
| class | `RawAux` | 252 | Store validated raw aux fields used by toolkit reports and adapters. |
| function | `to_dict` | 256 | Return a serializable dictionary representation. |
| class | `CoffSection` | 265 | Store validated coff section fields used by toolkit reports and adapters. |
| function | `is_comdat` | 282 | Execute the is comdat operation for the current toolkit workflow. |
| function | `comdat_selection_name` | 287 | Execute the comdat selection name operation for the current toolkit workflow. |
| function | `alignment_power` | 292 | Execute the alignment power operation for the current toolkit workflow. |
| function | `alignment` | 302 | Execute the alignment operation for the current toolkit workflow. |
| function | `to_dict` | 307 | Return a serializable dictionary representation. |
| class | `CoffSymbol` | 333 | Store validated coff symbol fields used by toolkit reports and adapters. |
| function | `is_function` | 345 | Execute the is function operation for the current toolkit workflow. |
| function | `section_definition` | 352 | Execute the section definition operation for the current toolkit workflow. |
| function | `function_definition` | 360 | Execute the function definition operation for the current toolkit workflow. |
| function | `weak_external` | 368 | Execute the weak external operation for the current toolkit workflow. |
| function | `to_dict` | 375 | Return a serializable dictionary representation. |
| class | `CoffObject` | 391 | Store validated coff object fields used by toolkit reports and adapters. |
| function | `architecture` | 404 | Execute the architecture operation for the current toolkit workflow. |
| function | `section` | 412 | Execute the section operation for the current toolkit workflow. |
| function | `find_symbols` | 418 | Execute the find symbols operation for the current toolkit workflow. |
| function | `symbol_by_index` | 425 | Execute the symbol by index operation for the current toolkit workflow. |
| function | `to_dict` | 429 | Return a serializable dictionary representation. |
| class | `ExtractedSymbol` | 448 | Store validated extracted symbol fields used by toolkit reports and adapters. |
| function | `to_dict` | 457 | Return a serializable dictionary representation. |
| class | `ComdatCandidate` | 470 | Store validated comdat candidate fields used by toolkit reports and adapters. |
| function | `to_dict` | 482 | Return a serializable dictionary representation. |
| class | `ComdatResolution` | 499 | Store validated comdat resolution fields used by toolkit reports and adapters. |
| function | `valid` | 506 | Execute the valid operation for the current toolkit workflow. |
| function | `to_dict` | 510 | Return a serializable dictionary representation. |
| class | `SyntheticSymbolSpec` | 522 | Store validated synthetic symbol spec fields used by toolkit reports and adapters. |
| class | `SyntheticSectionSpec` | 533 | Store validated synthetic section spec fields used by toolkit reports and adapters. |
| function | `_read_string_table` | 547 | Support read string table processing for internal toolkit callers. |
| function | `_string_at` | 562 | Support string at processing for internal toolkit callers. |
| function | `_decode_symbol_name` | 572 | Support decode symbol name processing for internal toolkit callers. |
| function | `_decode_section_name` | 580 | Support decode section name processing for internal toolkit callers. |
| function | `_parse_header` | 588 | Return variant, machine, sections, timestamp, symptr, symcount, |
| function | `_parse_auxiliary_records` | 642 | Support parse auxiliary records processing for internal toolkit callers. |
| function | `_read_addend` | 701 | Support read addend processing for internal toolkit callers. |
| function | `parse_coff_bytes` | 708 | Parse coff bytes for the current toolkit workflow. |
| function | `parse_coff` | 907 | Parse coff for the current toolkit workflow. |
| function | `extract_symbol` | 915 | Extract symbol for the current toolkit workflow. |
| function | `collect_comdat_candidates` | 971 | Execute the collect comdat candidates operation for the current toolkit workflow. |
| function | `resolve_comdats` | 999 | Resolve COMDAT groups using PE/COFF selection semantics. |
| function | `_encode_name` | 1100 | Support encode name processing for internal toolkit callers. |
| function | `_section_aux_bytes` | 1110 | Support section aux bytes processing for internal toolkit callers. |
| function | `build_synthetic_coff_object` | 1127 | Build a deterministic classic COFF object with multiple sections. |
| function | `synthetic_symbol_indices` | 1244 | Execute the synthetic symbol indices operation for the current toolkit workflow. |
| function | `build_synthetic_coff` | 1256 | Backward-compatible one-section synthetic COFF builder. |
| function | `build_comdat_coff` | 1296 | Build comdat coff for the current toolkit workflow. |
| function | `write_synthetic_coff` | 1362 | Write synthetic coff for the current toolkit workflow. |
| function | `write_synthetic_coff_object` | 1380 | Write synthetic coff object for the current toolkit workflow. |

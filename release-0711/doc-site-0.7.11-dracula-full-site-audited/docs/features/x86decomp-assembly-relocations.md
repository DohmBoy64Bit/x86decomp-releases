---
title: x86decomp.assembly.relocations
description: Module reference for x86decomp.assembly.relocations.
---

# `x86decomp.assembly.relocations`

- Area: `toolkit`
- Source path: `src/x86decomp/assembly/relocations.py`
- SHA-256: `bc19a023e373f5a64a2a2ffdcc9835e57fc65bd76ba8c6ca87f1855b0ccb66a1`
- Size: `16013` bytes
- Lines: `382`

## Module docstring

Provide the current runtime implementation for the `x86decomp.assembly.relocations` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `SymbolAddress` | 25 | Store validated symbol address fields used by toolkit reports and adapters. |
| function | `safe_name` | 34 | Execute the safe name operation for the current toolkit workflow. |
| function | `to_dict` | 38 | Return a serializable dictionary representation. |
| function | `normalize_symbol_map` | 49 | Normalize symbol map for the current toolkit workflow. |
| function | `supported_relocations` | 100 | Execute the supported relocations operation for the current toolkit workflow. |
| function | `_read_addend` | 121 | Support read addend processing for internal toolkit callers. |
| function | `_write_value` | 128 | Support write value processing for internal toolkit callers. |
| function | `_object_symbol_target` | 139 | Support object symbol target processing for internal toolkit callers. |
| function | `_resolve_target` | 161 | Support resolve target processing for internal toolkit callers. |
| function | `_compute_value` | 187 | Support compute value processing for internal toolkit callers. |
| class | `RelocationResolver` | 245 | Resolve COFF relocation fields under an explicit original-RVA symbol map. |
| function | `inspect` | 248 | Execute the inspect operation for the current toolkit workflow. |
| function | `resolve` | 269 | Resolve resolve for the current toolkit workflow. |

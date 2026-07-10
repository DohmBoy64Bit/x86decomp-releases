---
title: x86decomp.exe_diff
description: Module reference for x86decomp.exe_diff.
---

# `x86decomp.exe_diff`

- Area: `toolkit`
- Source path: `src/x86decomp/exe_diff.py`
- SHA-256: `c6ba882c4efd60db8e9cdf487bc13012257ca0be8f258030657ad87aba66ff48`
- Size: `8250` bytes
- Lines: `195`

## Module docstring

Executable-function versus COFF-symbol comparison for matching mode.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `rva_to_file_offset` | 16 | Execute the rva to file offset operation for the current toolkit workflow. |
| function | `extract_pe_bytes` | 33 | Extract pe bytes for the current toolkit workflow. |
| function | `_masked_copy` | 51 | Support masked copy processing for internal toolkit callers. |
| function | `_candidate_relocation_masks` | 61 | Support candidate relocation masks processing for internal toolkit callers. |
| function | `_pe_base_relocation_masks` | 78 | Support pe base relocation masks processing for internal toolkit callers. |
| function | `compare_pe_function_to_coff_symbol` | 89 | Compare pe function to coff symbol for the current toolkit workflow. |

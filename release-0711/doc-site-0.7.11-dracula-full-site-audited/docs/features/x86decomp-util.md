---
title: x86decomp.util
description: Module reference for x86decomp.util.
---

# `x86decomp.util`

- Area: `toolkit`
- Source path: `src/x86decomp/util.py`
- SHA-256: `a31791a06728eb30ecd156b1ab6f57dc3a56197be2ea6fe2043a2903228d9510`
- Size: `4349` bytes
- Lines: `126`

## Module docstring

Small, dependency-free utilities shared by all modules.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `utc_now` | 17 | Return a stable RFC 3339 UTC timestamp. |
| function | `sha256_bytes` | 22 | Execute the sha256 bytes operation for the current toolkit workflow. |
| function | `sha256_file` | 27 | Execute the sha256 file operation for the current toolkit workflow. |
| function | `canonical_json_bytes` | 36 | Execute the canonical json bytes operation for the current toolkit workflow. |
| function | `load_json` | 43 | Load and parse JSON content from a filesystem path. |
| function | `atomic_write_bytes` | 49 | Execute the atomic write bytes operation for the current toolkit workflow. |
| function | `atomic_write_text` | 66 | Execute the atomic write text operation for the current toolkit workflow. |
| function | `write_json` | 71 | Write json for the current toolkit workflow. |
| function | `copy_file_atomic` | 77 | Execute the copy file atomic operation for the current toolkit workflow. |
| function | `ensure_relative_path` | 92 | Resolve candidate and reject paths that escape root. |
| function | `require_mapping` | 103 | Execute the require mapping operation for the current toolkit workflow. |
| function | `require_string` | 110 | Execute the require string operation for the current toolkit workflow. |
| function | `require_int` | 118 | Execute the require int operation for the current toolkit workflow. |

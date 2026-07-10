---
title: x86decomp.angr_backend
description: Module reference for x86decomp.angr_backend.
---

# `x86decomp.angr_backend`

- Area: `toolkit`
- Source path: `src/x86decomp/angr_backend.py`
- SHA-256: `65a806874de433e75550e45759ce6ace0bf9fdcfdcf27fb179c3b90f73f9d0be`
- Size: `21555` bytes
- Lines: `468`

## Module docstring

Optional angr comparative symbolic execution backend for bounded code blobs.

The built-in symbolic engine remains the default deterministic backend. This
module integrates angr when installed and performs finite path comparison over
explicit input/output registers and stack arguments. Results are scoped to the
selected architecture, code blobs, path/step limits, and observable registers.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_load_angr` | 18 | Support load angr processing for internal toolkit callers. |
| function | `_arch_name` | 28 | Support arch name processing for internal toolkit callers. |
| function | `_summaries` | 37 | Support summaries processing for internal toolkit callers. |
| function | `_counterexample` | 113 | Support counterexample processing for internal toolkit callers. |
| function | `angr_bounded_compare` | 132 | Execute the angr bounded compare operation for the current toolkit workflow. |
| function | `angr_bounded_compare_files` | 178 | Execute the angr bounded compare files operation for the current toolkit workflow. |
| function | `_load_memory_harness` | 187 | Support load memory harness processing for internal toolkit callers. |
| function | `_memory_summaries` | 215 | Support memory summaries processing for internal toolkit callers. |
| function | `_memory_counterexample` | 383 | Support memory counterexample processing for internal toolkit callers. |
| function | `angr_memory_alias_compare` | 413 | Execute the angr memory alias compare operation for the current toolkit workflow. |
| function | `angr_memory_alias_compare_files` | 452 | Execute the angr memory alias compare files operation for the current toolkit workflow. |

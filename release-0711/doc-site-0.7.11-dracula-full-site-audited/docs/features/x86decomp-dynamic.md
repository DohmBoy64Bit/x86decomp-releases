---
title: x86decomp.dynamic
description: Module reference for x86decomp.dynamic.
---

# `x86decomp.dynamic`

- Area: `toolkit`
- Source path: `src/x86decomp/dynamic.py`
- SHA-256: `9b3cd201a5701bf48b73edd9e1a1984d4c6550d116e1a5b603453270c34ea4a8`
- Size: `15858` bytes
- Lines: `359`

## Module docstring

Bounded differential execution using Unicorn.

This validator is intentionally explicit about its execution envelope. It can
compare leaf routines and routines whose external calls are represented by
user-supplied deterministic stubs. It does not model a complete Windows process.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_unicorn` | 21 | Support unicorn processing for internal toolkit callers. |
| function | `_align_down` | 33 | Support align down processing for internal toolkit callers. |
| function | `_align_up` | 38 | Support align up processing for internal toolkit callers. |
| class | `MemoryRegion` | 44 | Store validated memory region fields used by toolkit reports and adapters. |
| class | `ExecutionSpec` | 52 | Store validated execution spec fields used by toolkit reports and adapters. |
| function | `load_execution_spec` | 69 | Load execution spec for the current toolkit workflow. |
| function | `_register_map` | 157 | Support register map processing for internal toolkit callers. |
| function | `_map_region` | 175 | Support map region processing for internal toolkit callers. |
| function | `execute_code` | 188 | Execute the execute code operation for the current toolkit workflow. |
| function | `code_hook` | 232 | Execute the code hook operation for the current toolkit workflow. |
| function | `differential_validate` | 290 | Execute the differential validate operation for the current toolkit workflow. |
| function | `differential_validate_files` | 339 | Execute the differential validate files operation for the current toolkit workflow. |

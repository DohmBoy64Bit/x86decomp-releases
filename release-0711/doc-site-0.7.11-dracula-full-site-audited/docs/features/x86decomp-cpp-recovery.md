---
title: x86decomp.cpp_recovery
description: Module reference for x86decomp.cpp_recovery.
---

# `x86decomp.cpp_recovery`

- Area: `toolkit`
- Source path: `src/x86decomp/cpp_recovery.py`
- SHA-256: `354295c6c6a16f6b8296760d153c824945f8f46bb035e843805d0979c5a55a3e`
- Size: `8186` bytes
- Lines: `199`

## Module docstring

Bounded C++ relationship recovery from MSVC metadata and code patterns.

The output distinguishes directly parsed metadata from derived candidates.  It
never claims original source declarations, access modifiers, or method names.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_function_prefix` | 18 | Support function prefix processing for internal toolkit callers. |
| function | `_adjustor_thunk_candidate` | 28 | Support adjustor thunk candidate processing for internal toolkit callers. |
| function | `recover_cpp_model` | 56 | Execute the recover cpp model operation for the current toolkit workflow. |

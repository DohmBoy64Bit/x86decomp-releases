---
title: x86decomp.harness_generator
description: Module reference for x86decomp.harness_generator.
---

# `x86decomp.harness_generator`

- Area: `toolkit`
- Source path: `src/x86decomp/harness_generator.py`
- SHA-256: `a5d1bf5ac1fc22d34e2975ee93d73e021345d641ef883bc2bd3e2b9638179fe4`
- Size: `7169` bytes
- Lines: `165`

## Module docstring

Generate bounded differential-execution harnesses from explicit ABI facts.

Generated values are deterministic test inputs, not recovered original inputs.
Pointer regions are allocated only when the user declares pointer parameters.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_deterministic_word` | 17 | Support deterministic word processing for internal toolkit callers. |
| function | `generate_execution_harness` | 23 | Generate execution harness for the current toolkit workflow. |
| function | `generate_execution_harness_from_files` | 141 | Generate execution harness from files for the current toolkit workflow. |

---
title: x86decomp_testkit.models
description: Module reference for x86decomp_testkit.models.
---

# `x86decomp_testkit.models`

- Area: `test-suite`
- Source path: `test-suite/src/x86decomp_testkit/models.py`
- SHA-256: `cd3c09bfe5c1f30f8693c64b7a6f9b8ae0f4ce6cff40a82f9b8c42b5a1bea00c`
- Size: `4728` bytes
- Lines: `143`

## Module docstring

Provide the installed test-suite implementation for the `x86decomp_testkit.models` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `Status` | 10 | Enumerate supported status values. |
| class | `AdapterKind` | 18 | Enumerate supported adapter kind values. |
| class | `ProbeResult` | 28 | Store validated probe result fields used by toolkit reports and adapters. |
| function | `to_dict` | 38 | Return a serializable dictionary representation. |
| class | `AdapterSpec` | 44 | Store validated adapter spec fields used by toolkit reports and adapters. |
| class | `TestResult` | 66 | Store validated test result fields used by toolkit reports and adapters. |
| function | `to_dict` | 82 | Return a serializable dictionary representation. |
| class | `RunSummary` | 90 | Store validated run summary fields used by toolkit reports and adapters. |
| function | `counts` | 104 | Execute the counts operation for the current toolkit workflow. |
| function | `exit_code` | 111 | Execute the exit code operation for the current toolkit workflow. |
| function | `to_dict` | 120 | Return a serializable dictionary representation. |
| function | `normalized_path` | 140 | Normalize d path for the current toolkit workflow. |

---
title: x86decomp.workflow
description: Module reference for x86decomp.workflow.
---

# `x86decomp.workflow`

- Area: `toolkit`
- Source path: `src/x86decomp/workflow.py`
- SHA-256: `7f8feb468bf53f4cd1d5bc98cec7da39a21ebab9ee9483284d10052453129553`
- Size: `10092` bytes
- Lines: `236`

## Module docstring

Per-function decompilation mode and validation-state management.

The workflow intentionally keeps matching and functional progress independent.
A function can be byte matched but not functionally exercised, or behaviorally
validated without reproducing the original instruction stream.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `DecompilationMode` | 21 | Coordinate decompilation mode behavior for the current toolkit workflow. |
| class | `SourceStage` | 27 | Coordinate source stage behavior for the current toolkit workflow. |
| class | `MatchingStatus` | 36 | Coordinate matching status behavior for the current toolkit workflow. |
| class | `FunctionalStatus` | 49 | Coordinate functional status behavior for the current toolkit workflow. |
| class | `FunctionWorkflow` | 69 | Store validated function workflow fields used by toolkit reports and adapters. |
| function | `to_dict` | 84 | Return a serializable dictionary representation. |
| function | `from_dict` | 101 | Execute the from dict operation for the current toolkit workflow. |
| function | `_state_path` | 133 | Support state path processing for internal toolkit callers. |
| function | `initialize_function_workflow` | 139 | Initialize function workflow for the current toolkit workflow. |
| function | `load_function_workflow` | 170 | Load function workflow for the current toolkit workflow. |
| function | `save_function_workflow` | 178 | Execute the save function workflow operation for the current toolkit workflow. |
| function | `update_function_workflow` | 184 | Update function workflow for the current toolkit workflow. |

---
title: x86decomp.governance.hypotheses
description: Module reference for x86decomp.governance.hypotheses.
---

# `x86decomp.governance.hypotheses`

- Area: `toolkit`
- Source path: `src/x86decomp/governance/hypotheses.py`
- SHA-256: `8fe031d32f8bad8b396772ae5ae48ee101e0069a767e6fefab8790ff6a5fce95`
- Size: `13879` bytes
- Lines: `264`

## Module docstring

Provide the current runtime implementation for the `x86decomp.governance.hypotheses` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `Hypothesis` | 38 | Store validated hypothesis fields used by toolkit reports and adapters. |
| function | `_row_to_hypothesis` | 53 | Support row to hypothesis processing for internal toolkit callers. |
| class | `HypothesisLedger` | 70 | Coordinate hypothesis ledger behavior for the current toolkit workflow. |
| function | `__init__` | 72 | Initialize the instance with validated constructor state. |
| function | `create` | 77 | Create create for the current toolkit workflow. |
| function | `get` | 100 | Execute the get operation for the current toolkit workflow. |
| function | `list` | 108 | Execute the list operation for the current toolkit workflow. |
| function | `add_dependency` | 125 | Execute the add dependency operation for the current toolkit workflow. |
| function | `_has_dependency_cycle` | 137 | Support has dependency cycle processing for internal toolkit callers. |
| function | `attach_evidence` | 149 | Execute the attach evidence operation for the current toolkit workflow. |
| function | `_recalculate_confidence` | 180 | Support recalculate confidence processing for internal toolkit callers. |
| function | `transition` | 198 | Execute the transition operation for the current toolkit workflow. |
| function | `acceptance_gate` | 221 | Execute the acceptance gate operation for the current toolkit workflow. |
| function | `describe` | 255 | Execute the describe operation for the current toolkit workflow. |

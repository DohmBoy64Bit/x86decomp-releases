---
title: x86decomp.release_gate
description: Module reference for x86decomp.release_gate.
---

# `x86decomp.release_gate`

- Area: `toolkit`
- Source path: `src/x86decomp/release_gate.py`
- SHA-256: `381121856f0ce249fe7e268be5f57d20bc6b7bc31b05c26b4056796629bce9c7`
- Size: `8215` bytes
- Lines: `172`

## Module docstring

Target release acceptance gate.

The gate aggregates exact project-state, evidence, workflow, pipeline,
reproducibility, security, and image-convergence records.  It never upgrades a
missing report into a pass and never treats the three-source rule as a guarantee
of semantic truth.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_workflow_gate` | 31 | Support workflow gate processing for internal toolkit callers. |
| function | `_claim_gate` | 65 | Support claim gate processing for internal toolkit callers. |
| function | `_pipeline_gate` | 79 | Support pipeline gate processing for internal toolkit callers. |
| function | `evaluate_release_gate` | 94 | Execute the evaluate release gate operation for the current toolkit workflow. |

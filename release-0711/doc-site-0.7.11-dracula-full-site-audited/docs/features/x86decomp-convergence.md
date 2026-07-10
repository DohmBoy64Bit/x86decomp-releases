---
title: x86decomp.convergence
description: Module reference for x86decomp.convergence.
---

# `x86decomp.convergence`

- Area: `toolkit`
- Source path: `src/x86decomp/convergence.py`
- SHA-256: `fdc0f36afb90be8d0a8724878be24d104a662e1f4515850516810894228d1725`
- Size: `7576` bytes
- Lines: `177`

## Module docstring

Target-specific whole-image convergence analysis.

The engine classifies observed differences and ranks next actions.  It never
claims causality unless the mismatch falls inside a declared PE field or
normalization range.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_section_kind` | 20 | Support section kind processing for internal toolkit callers. |
| function | `analyze_image_convergence` | 36 | Execute the analyze image convergence operation for the current toolkit workflow. |
| function | `append_convergence_history` | 167 | Append convergence history for the current toolkit workflow. |

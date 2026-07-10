---
title: x86decomp.reproducibility
description: Module reference for x86decomp.reproducibility.
---

# `x86decomp.reproducibility`

- Area: `toolkit`
- Source path: `src/x86decomp/reproducibility.py`
- SHA-256: `42890412018863aa16c5913570286c5bb71ef865e55a1b8f6de59e4618cab6ed`
- Size: `6610` bytes
- Lines: `161`

## Module docstring

Reproducibility manifests and verification.

The report records what can be reproduced, what is missing, and why.  A missing
external tool is never treated as a successful reproduction.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_version` | 24 | Support version processing for internal toolkit callers. |
| function | `build_reproduction_manifest` | 51 | Build reproduction manifest for the current toolkit workflow. |
| function | `verify_reproduction_manifest` | 120 | Verify reproduction manifest for the current toolkit workflow. |

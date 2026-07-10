---
title: x86decomp.relink
description: Module reference for x86decomp.relink.
---

# `x86decomp.relink`

- Area: `toolkit`
- Source path: `src/x86decomp/relink.py`
- SHA-256: `b4ea5875ec158515fc1a9408a7c1b46845e605cb2e8f4ea9548bc6b052d76cbd`
- Size: `5748` bytes
- Lines: `124`

## Module docstring

Manifest-driven full-image relink backend.

The backend performs a real linker invocation using user-supplied objects and a
linker profile. It does not claim to infer the original linker script or object
partitioning automatically.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `run_full_relink` | 23 | Run full relink for the current toolkit workflow. |

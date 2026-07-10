---
title: x86decomp.patching
description: Module reference for x86decomp.patching.
---

# `x86decomp.patching`

- Area: `toolkit`
- Source path: `src/x86decomp/patching.py`
- SHA-256: `f81a6e2fc12323262049645808778be12227704ee0f0d36eb343e946e56b3822`
- Size: `4276` bytes
- Lines: `99`

## Module docstring

Patch-image backend with integrity checks and PE checksum refresh.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_checksum_offset` | 15 | Support checksum offset processing for internal toolkit callers. |
| function | `calculate_pe_checksum` | 25 | Execute the calculate pe checksum operation for the current toolkit workflow. |
| function | `patch_pe_function` | 41 | Execute the patch pe function operation for the current toolkit workflow. |

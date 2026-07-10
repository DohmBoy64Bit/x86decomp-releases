---
title: x86decomp.objdiff_adapter
description: Module reference for x86decomp.objdiff_adapter.
---

# `x86decomp.objdiff_adapter`

- Area: `toolkit`
- Source path: `src/x86decomp/objdiff_adapter.py`
- SHA-256: `a8e9ce06780f783f2ad9c6e50cf106fd0ecc1b82052d39fbbeeb1f40632a7d4b`
- Size: `7822` bytes
- Lines: `174`

## Module docstring

Version-agnostic, manifest-driven objdiff CLI integration.

objdiff's CLI/configuration evolves independently. This adapter executes an explicit
argument array, captures provenance, and imports a declared JSON/text output without
hard-coding unstable flags. It is a real external-tool boundary, not a fake diff.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_resolve_executable` | 24 | Support resolve executable processing for internal toolkit callers. |
| function | `run_objdiff_manifest` | 39 | Run objdiff manifest for the current toolkit workflow. |

---
title: x86decomp.ground_truth
description: Module reference for x86decomp.ground_truth.
---

# `x86decomp.ground_truth`

- Area: `toolkit`
- Source path: `src/x86decomp/ground_truth.py`
- SHA-256: `8e4ada1866c092d9594a5478abc51ee6d17de7cb2a344e8e29e7115906ab4eef`
- Size: `17274` bytes
- Lines: `366`

## Module docstring

Reproducible compiler/version ground-truth corpus builder.

The corpus records source hashes, compiler hashes and versions, complete command
lines, environment policy, COFF structure, symbols, COMDAT metadata, and output
hashes.  It is designed to compare compiler generations without redistributing
proprietary toolchains: users register their own compiler executables.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_resolve_executable` | 24 | Support resolve executable processing for internal toolkit callers. |
| function | `_version` | 37 | Support version processing for internal toolkit callers. |
| function | `_expand_flag_matrix` | 48 | Support expand flag matrix processing for internal toolkit callers. |
| function | `build_ground_truth_corpus` | 75 | Build ground truth corpus for the current toolkit workflow. |
| function | `verify_ground_truth_corpus` | 195 | Verify ground truth corpus for the current toolkit workflow. |
| function | `compare_ground_truth_corpora` | 216 | Compare successful corpus builds across compiler/version reports. |
| function | `create_builtin_manifest` | 298 | Create builtin manifest for the current toolkit workflow. |

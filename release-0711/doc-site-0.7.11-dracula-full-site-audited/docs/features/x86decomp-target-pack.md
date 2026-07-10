---
title: x86decomp.target_pack
description: Module reference for x86decomp.target_pack.
---

# `x86decomp.target_pack`

- Area: `toolkit`
- Source path: `src/x86decomp/target_pack.py`
- SHA-256: `113aae1251f1143cc8a6f2a4e32adc05fbef2afb3a98bca0bbf588ae129ab8e9`
- Size: `19244` bytes
- Lines: `434`

## Module docstring

Target-pack inference, validation, and project-template generation.

A target pack records observed facts and user-supplied decisions separately.
Inferences never invent compiler versions, linker flags, names, or source layout.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `SupportingArtifact` | 30 | Store validated supporting artifact fields used by toolkit reports and adapters. |
| function | `to_dict` | 37 | Return a serializable dictionary representation. |
| function | `_toml_string` | 42 | Support toml string processing for internal toolkit callers. |
| function | `_write_target_toml` | 47 | Support write target toml processing for internal toolkit callers. |
| function | `_safe_artifact` | 90 | Support safe artifact processing for internal toolkit callers. |
| function | `infer_target_pack` | 98 | Execute the infer target pack operation for the current toolkit workflow. |
| function | `load_target_pack` | 308 | Load target pack for the current toolkit workflow. |
| function | `verify_target_pack` | 320 | Verify target pack for the current toolkit workflow. |
| function | `generate_project_from_target_pack` | 351 | Generate project from target pack for the current toolkit workflow. |

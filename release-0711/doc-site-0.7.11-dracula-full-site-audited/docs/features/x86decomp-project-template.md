---
title: x86decomp.project_template
description: Module reference for x86decomp.project_template.
---

# `x86decomp.project_template`

- Area: `toolkit`
- Source path: `src/x86decomp/project_template.py`
- SHA-256: `21050aad81e374bafd2400628ea946f8bc3040ddd735d6ea4299b7a33604d589`
- Size: `8817` bytes
- Lines: `194`

## Module docstring

Grounded project-template generation from a verified target pack.

Templates create executable workflow/configuration surfaces, never fabricated
source code.  Unknown compiler, language, linker, or layout facts remain
explicitly unresolved and are not converted into fake profiles or build files.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_artifact_roles` | 20 | Support artifact roles processing for internal toolkit callers. |
| function | `derive_template_contract` | 25 | Derive a target project shape only from recorded facts and decisions. |
| function | `_write_project_helper` | 88 | Support write project helper processing for internal toolkit callers. |
| function | `materialize_project_template` | 133 | Create a deterministic, non-fabricated project working layout. |

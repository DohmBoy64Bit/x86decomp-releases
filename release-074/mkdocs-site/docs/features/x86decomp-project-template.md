---
title: x86decomp.project_template
description: Grounded project-template generation from a verified target pack.
original_path: features/x86decomp-project-template.html
---

<a id="function-artifact-roles"></a>
<a id="function-derive-template-contract"></a>
<a id="function-write-project-helper"></a>
<a id="function-materialize-project-template"></a>

Section: Source-derived feature and function reference

# x86decomp.project_template

Grounded project-template generation from a verified target pack.

Metadata: core · current · 4 functions/methods

**Source:** `src/x86decomp/project_template.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `2a70050138d13bf73d963a6cb49d404b39c2d12dbc00298e7e1a79999d076f8f`.

## Functions and methods

Metadata: internal · line 21

### _artifact_roles

No function or method docstring is declared in the v0.7.4 source.

```
def _artifact_roles(pack: dict[str, Any]) -> set[str]
```

**Catalog symbol:** `x86decomp.project_template:_artifact_roles`

Metadata: public · line 25

### derive_template_contract

Derive a target project shape only from recorded facts and decisions.

```
def derive_template_contract(target_pack: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_template:derive_template_contract`

Metadata: internal · line 88

### _write_project_helper

No function or method docstring is declared in the v0.7.4 source.

```
def _write_project_helper(path: Path) -> None
```

**Catalog symbol:** `x86decomp.project_template:_write_project_helper`

Metadata: public · line 133

### materialize_project_template

Create a deterministic, non-fabricated project working layout.

```
def materialize_project_template(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_template:materialize_project_template`

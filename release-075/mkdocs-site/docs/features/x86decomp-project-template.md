---
title: x86decomp.project_template
description: Grounded project-template generation from a verified target pack.
---

# `x86decomp.project_template`

Grounded project-template generation from a verified target pack.

Templates create executable workflow/configuration surfaces, never fabricated
source code.  Unknown compiler, language, linker, or layout facts remain
explicitly unresolved and are not converted into fake profiles or build files.

**Area:** Toolkit  
**Source:** `src/x86decomp/project_template.py`  
**SHA-256:** `2a70050138d13bf73d963a6cb49d404b39c2d12dbc00298e7e1a79999d076f8f`  
**Functions/methods:** 4

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-artifact-roles"></a>

### `_artifact_roles`

No function or method docstring is declared in the 0.7.5 source.

```python
def _artifact_roles(pack: dict[str, Any]) -> set[str]
```

**Catalog symbol:** `x86decomp.project_template:_artifact_roles`  
**Visibility:** internal  
**Source line:** 21

<a id="function-derive-template-contract"></a>

### `derive_template_contract`

Derive a target project shape only from recorded facts and decisions.

```python
def derive_template_contract(target_pack: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_template:derive_template_contract`  
**Visibility:** public  
**Source line:** 25

<a id="function-write-project-helper"></a>

### `_write_project_helper`

No function or method docstring is declared in the 0.7.5 source.

```python
def _write_project_helper(path: Path) -> None
```

**Catalog symbol:** `x86decomp.project_template:_write_project_helper`  
**Visibility:** internal  
**Source line:** 88

<a id="function-materialize-project-template"></a>

### `materialize_project_template`

Create a deterministic, non-fabricated project working layout.

```python
def materialize_project_template(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_template:materialize_project_template`  
**Visibility:** public  
**Source line:** 133

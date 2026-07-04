---
title: x86decomp.project
description: Project initialization, architecture dispatch, and integrity verification.
---

# `x86decomp.project`

Project initialization, architecture dispatch, and integrity verification.

**Area:** Toolkit  
**Source:** `src/x86decomp/project.py`  
**SHA-256:** `7abbde69cd90fa6fff97d8fa42d991c4640a6eccbd2c096b76f7ebc4d74195c7`  
**Functions/methods:** 4

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-initialize-project"></a>

### `initialize_project`

No function or method docstring is declared in the 0.7.5 source.

```python
def initialize_project(binary: Path, project_root: Path, *, copy_binary: bool=True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project:initialize_project`  
**Visibility:** public  
**Source line:** 61

<a id="function-resolve-binary-path"></a>

### `_resolve_binary_path`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_binary_path(root: Path, project: dict[str, Any]) -> Path
```

**Catalog symbol:** `x86decomp.project:_resolve_binary_path`  
**Visibility:** internal  
**Source line:** 151

<a id="function-verify-project"></a>

### `verify_project`

No function or method docstring is declared in the 0.7.5 source.

```python
def verify_project(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project:verify_project`  
**Visibility:** public  
**Source line:** 164

<a id="function-require-valid-project"></a>

### `require_valid_project`

No function or method docstring is declared in the 0.7.5 source.

```python
def require_valid_project(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project:require_valid_project`  
**Visibility:** public  
**Source line:** 223

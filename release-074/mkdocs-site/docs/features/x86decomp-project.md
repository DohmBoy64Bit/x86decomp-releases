---
title: x86decomp.project
description: Project initialization, architecture dispatch, and integrity verification.
original_path: features/x86decomp-project.html
---

<a id="function-initialize-project"></a>
<a id="function-resolve-binary-path"></a>
<a id="function-verify-project"></a>
<a id="function-require-valid-project"></a>

Section: Source-derived feature and function reference

# x86decomp.project

Project initialization, architecture dispatch, and integrity verification.

Metadata: core · current · 4 functions/methods

**Source:** `src/x86decomp/project.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `a9077107216cddb15d5e0a7ab95ac0e6f63b0817c2d1329842b6b4792f11ec5f`.

## Functions and methods

Metadata: public · line 61

### initialize_project

No function or method docstring is declared in the v0.7.4 source.

```
def initialize_project(binary: Path, project_root: Path, *, copy_binary: bool = True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project:initialize_project`

Metadata: internal · line 151

### _resolve_binary_path

No function or method docstring is declared in the v0.7.4 source.

```
def _resolve_binary_path(root: Path, project: dict[str, Any]) -> Path
```

**Catalog symbol:** `x86decomp.project:_resolve_binary_path`

Metadata: public · line 164

### verify_project

No function or method docstring is declared in the v0.7.4 source.

```
def verify_project(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project:verify_project`

Metadata: public · line 223

### require_valid_project

No function or method docstring is declared in the v0.7.4 source.

```
def require_valid_project(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project:require_valid_project`

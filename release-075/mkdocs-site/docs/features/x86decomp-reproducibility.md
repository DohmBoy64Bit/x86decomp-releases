---
title: x86decomp.reproducibility
description: Reproducibility manifests and verification.
---

# `x86decomp.reproducibility`

Reproducibility manifests and verification.

The report records what can be reproduced, what is missing, and why.  A missing
external tool is never treated as a successful reproduction.

**Area:** Toolkit  
**Source:** `src/x86decomp/reproducibility.py`  
**SHA-256:** `bcc5e2a773d7eb7589f28df90c0fe898155788b8e695d15e363e6dbad249ae7b`  
**Functions/methods:** 3

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-version"></a>

### `_version`

No function or method docstring is declared in the 0.7.5 source.

```python
def _version(executable: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reproducibility:_version`  
**Visibility:** internal  
**Source line:** 26

<a id="function-build-reproduction-manifest"></a>

### `build_reproduction_manifest`

No function or method docstring is declared in the 0.7.5 source.

```python
def build_reproduction_manifest(project_root: Path, *, output: Path | None=None, required_tools: list[str] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reproducibility:build_reproduction_manifest`  
**Visibility:** public  
**Source line:** 52

<a id="function-verify-reproduction-manifest"></a>

### `verify_reproduction_manifest`

No function or method docstring is declared in the 0.7.5 source.

```python
def verify_reproduction_manifest(project_root: Path, manifest_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reproducibility:verify_reproduction_manifest`  
**Visibility:** public  
**Source line:** 120

---
title: x86decomp.objdiff_adapter
description: Version-agnostic, manifest-driven objdiff CLI integration.
---

# `x86decomp.objdiff_adapter`

Version-agnostic, manifest-driven objdiff CLI integration.

objdiff's CLI/configuration evolves independently. This adapter executes an explicit
argument array, captures provenance, and imports a declared JSON/text output without
hard-coding unstable flags. It is a real external-tool boundary, not a fake diff.

**Area:** Toolkit  
**Source:** `src/x86decomp/objdiff_adapter.py`  
**SHA-256:** `d312150b8b06b0e9b1656df7dab0a10e0e4a4db6047a4e83663875387b3851c1`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-resolve-executable"></a>

### `_resolve_executable`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_executable(value: Any) -> str
```

**Catalog symbol:** `x86decomp.objdiff_adapter:_resolve_executable`  
**Visibility:** internal  
**Source line:** 24

<a id="function-run-objdiff-manifest"></a>

### `run_objdiff_manifest`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_objdiff_manifest(manifest_path: Path, *, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.objdiff_adapter:run_objdiff_manifest`  
**Visibility:** public  
**Source line:** 38

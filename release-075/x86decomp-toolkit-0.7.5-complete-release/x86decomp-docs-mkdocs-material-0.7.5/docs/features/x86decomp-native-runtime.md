---
title: x86decomp.native.runtime
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.native.runtime`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/native/runtime.py`  
**SHA-256:** `42a582f61d69ef1bc07096d003f19db4c0598d7386be494c124cf4272b1aa854`  
**Functions/methods:** 5

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-runtimevalidation-init"></a>

### `RuntimeValidation.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def RuntimeValidation.__init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.__init__`  
**Visibility:** internal  
**Source line:** 15

<a id="function-runtimevalidation-validate-image"></a>

### `RuntimeValidation.validate_image`

No function or method docstring is declared in the 0.7.5 source.

```python
def RuntimeValidation.validate_image(self, image_path: Path, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.validate_image`  
**Visibility:** public  
**Source line:** 17

<a id="function-runtimevalidation-launch"></a>

### `RuntimeValidation.launch`

No function or method docstring is declared in the 0.7.5 source.

```python
def RuntimeValidation.launch(self, image_path: Path, *, execute: bool=False, timeout_seconds: int=10, arguments: list[str] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.launch`  
**Visibility:** public  
**Source line:** 29

<a id="function-runtimevalidation-map-crash"></a>

### `RuntimeValidation.map_crash`

No function or method docstring is declared in the 0.7.5 source.

```python
def RuntimeValidation.map_crash(self, rva: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.map_crash`  
**Visibility:** public  
**Source line:** 44

<a id="function-runtimevalidation-record"></a>

### `RuntimeValidation._record`

No function or method docstring is declared in the 0.7.5 source.

```python
def RuntimeValidation._record(self, path: Path, kind: str, checks: dict[str, Any], details: dict[str, Any], authorized: bool, actor: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation._record`  
**Visibility:** internal  
**Source line:** 50

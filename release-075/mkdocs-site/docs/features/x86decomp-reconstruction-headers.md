---
title: x86decomp.reconstruction.headers
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.headers`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/headers.py`  
**SHA-256:** `438c0233df3581b7634dd878b01f5b32f6918d7dac836115ad7bc1c0c50fdacc`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-headermanager-init"></a>

### `HeaderManager.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.__init__`  
**Visibility:** internal  
**Source line:** 10

<a id="function-headermanager-create"></a>

### `HeaderManager.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.create(self, path: str, *, visibility: str='private', actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.create`  
**Visibility:** public  
**Source line:** 11

<a id="function-headermanager-declare"></a>

### `HeaderManager.declare`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.declare(self, header_id: str, symbol_id: str, declaration: str, *, kind: str='function', confidence: float=1.0, evidence: list[dict[str, Any]] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.declare`  
**Visibility:** public  
**Source line:** 20

<a id="function-headermanager-include"></a>

### `HeaderManager.include`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.include(self, source_header_id: str, target_header_id: str, *, reason: str, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.include`  
**Visibility:** public  
**Source line:** 30

<a id="function-headermanager-cycles"></a>

### `HeaderManager.cycles`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.cycles(self, *, connection=None) -> list[list[str]]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.cycles`  
**Visibility:** public  
**Source line:** 37

<a id="function-headermanager-show"></a>

### `HeaderManager.show`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.show(self, header_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.show`  
**Visibility:** public  
**Source line:** 55

<a id="function-headermanager-synthesize"></a>

### `HeaderManager.synthesize`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.synthesize(self, header_id: str, *, output_root: str | Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.synthesize`  
**Visibility:** public  
**Source line:** 62

<a id="function-headermanager-validate"></a>

### `HeaderManager.validate`

No function or method docstring is declared in the 0.7.5 source.

```python
def HeaderManager.validate(self, header_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.validate`  
**Visibility:** public  
**Source line:** 73

---
title: x86decomp.memory
description: Append-only, hash-chained project memory.
---

# `x86decomp.memory`

Append-only, hash-chained project memory.

**Area:** Toolkit  
**Source:** `src/x86decomp/memory.py`  
**SHA-256:** `4fd6948418a67ffdd502b92649a5b18af16376b55272018305b59d5cddcad813`  
**Functions/methods:** 6

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-projectmemory-init"></a>

### `ProjectMemory.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectMemory.__init__(self, project_root: Path)
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.__init__`  
**Visibility:** internal  
**Source line:** 15

<a id="function-projectmemory-read-events"></a>

### `ProjectMemory.read_events`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectMemory.read_events(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.read_events`  
**Visibility:** public  
**Source line:** 24

<a id="function-projectmemory-append"></a>

### `ProjectMemory.append`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectMemory.append(self, *, actor: str, category: str, summary: str, details: dict[str, Any] | None=None, evidence_ids: Iterable[str]=()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.append`  
**Visibility:** public  
**Source line:** 41

<a id="function-projectmemory-verify"></a>

### `ProjectMemory.verify`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectMemory.verify(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.verify`  
**Visibility:** public  
**Source line:** 73

<a id="function-projectmemory-require-valid"></a>

### `ProjectMemory.require_valid`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectMemory.require_valid(self) -> None
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.require_valid`  
**Visibility:** public  
**Source line:** 91

<a id="function-projectmemory-render"></a>

### `ProjectMemory.render`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectMemory.render(self) -> str
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.render`  
**Visibility:** public  
**Source line:** 96

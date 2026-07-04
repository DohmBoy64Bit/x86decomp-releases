---
title: x86decomp.governance.counterexamples
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.counterexamples`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/counterexamples.py`  
**SHA-256:** `2223bd0eec9a09b58739850670b5d3434dfce554a3578cbe2ab870e43e698096`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-counterexamplestore-init"></a>

### `CounterexampleStore.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def CounterexampleStore.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.__init__`  
**Visibility:** internal  
**Source line:** 15

<a id="function-counterexamplestore-add"></a>

### `CounterexampleStore.add`

No function or method docstring is declared in the 0.7.5 source.

```python
def CounterexampleStore.add(self, scope_kind: str, scope_id: str, payload: bytes | str | Path, *, predicate: dict[str, Any], provenance: dict[str, Any] | None=None, actor: str='validator') -> str
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.add`  
**Visibility:** public  
**Source line:** 20

<a id="function-counterexamplestore-minimize"></a>

### `CounterexampleStore.minimize`

No function or method docstring is declared in the 0.7.5 source.

```python
def CounterexampleStore.minimize(self, counterexample_id: str, predicate: Predicate, *, actor: str='validator', max_tests: int=10000) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.minimize`  
**Visibility:** public  
**Source line:** 38

<a id="function-counterexamplestore-promote-to-regression"></a>

### `CounterexampleStore.promote_to_regression`

No function or method docstring is declared in the 0.7.5 source.

```python
def CounterexampleStore.promote_to_regression(self, counterexample_id: str, destination_root: str | Path, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.promote_to_regression`  
**Visibility:** public  
**Source line:** 63

<a id="function-counterexamplestore-get"></a>

### `CounterexampleStore.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def CounterexampleStore.get(self, counterexample_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.get`  
**Visibility:** public  
**Source line:** 79

<a id="function-counterexamplestore-list"></a>

### `CounterexampleStore.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def CounterexampleStore.list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.list`  
**Visibility:** public  
**Source line:** 90

<a id="function-ddmin-bytes"></a>

### `ddmin_bytes`

Delta-debug a byte string while preserving predicate(data) == True.

```python
def ddmin_bytes(data: bytes, predicate: Predicate, *, max_tests: int=10000) -> tuple[bytes, int]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:ddmin_bytes`  
**Visibility:** public  
**Source line:** 96

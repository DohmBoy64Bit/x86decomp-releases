---
title: x86decomp.governance.reviews
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.reviews`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/reviews.py`  
**SHA-256:** `ba9d5d2757485bdcfdb2ed1255287013fe710def654fcbc2cf8a6801fe25312f`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-reviewqueue-init"></a>

### `ReviewQueue.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ReviewQueue.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.__init__`  
**Visibility:** internal  
**Source line:** 13

<a id="function-reviewqueue-create"></a>

### `ReviewQueue.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def ReviewQueue.create(self, kind: str, subject_id: str, summary: str, *, priority: int=50, details: dict[str, Any] | None=None, actor: str='system') -> str
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.create`  
**Visibility:** public  
**Source line:** 17

<a id="function-reviewqueue-assign"></a>

### `ReviewQueue.assign`

No function or method docstring is declared in the 0.7.5 source.

```python
def ReviewQueue.assign(self, review_id: str, assignee: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.assign`  
**Visibility:** public  
**Source line:** 30

<a id="function-reviewqueue-decide"></a>

### `ReviewQueue.decide`

No function or method docstring is declared in the 0.7.5 source.

```python
def ReviewQueue.decide(self, review_id: str, decision: str, rationale: str, *, actor: str='analyst', lock: bool=False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.decide`  
**Visibility:** public  
**Source line:** 44

<a id="function-reviewqueue-lock"></a>

### `ReviewQueue.lock`

No function or method docstring is declared in the 0.7.5 source.

```python
def ReviewQueue.lock(self, review_id: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.lock`  
**Visibility:** public  
**Source line:** 69

<a id="function-reviewqueue-get"></a>

### `ReviewQueue.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def ReviewQueue.get(self, review_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.get`  
**Visibility:** public  
**Source line:** 78

<a id="function-reviewqueue-list"></a>

### `ReviewQueue.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def ReviewQueue.list(self, *, status: str | None=None, limit: int=100) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.list`  
**Visibility:** public  
**Source line:** 90

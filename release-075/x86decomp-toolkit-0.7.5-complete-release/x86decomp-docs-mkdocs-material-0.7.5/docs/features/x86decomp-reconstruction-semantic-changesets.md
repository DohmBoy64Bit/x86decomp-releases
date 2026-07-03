---
title: x86decomp.reconstruction.semantic_changesets
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.semantic_changesets`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/semantic_changesets.py`  
**SHA-256:** `4342cc6206f76716dcc2007d36fd18ed0aff99cd7ebb562ef544adeeb8a537f3`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-semanticchangesets-init"></a>

### `SemanticChangeSets.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.__init__`  
**Visibility:** internal  
**Source line:** 9

<a id="function-semanticchangesets-create"></a>

### `SemanticChangeSets.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.create(self, name: str, *, base_audit_hash: str | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.create`  
**Visibility:** public  
**Source line:** 10

<a id="function-semanticchangesets-get"></a>

### `SemanticChangeSets.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.get(self, changeset_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.get`  
**Visibility:** public  
**Source line:** 15

<a id="function-semanticchangesets-add-operation"></a>

### `SemanticChangeSets.add_operation`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.add_operation(self, changeset_id: str, operation: dict[str, Any], *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.add_operation`  
**Visibility:** public  
**Source line:** 21

<a id="function-semanticchangesets-merge"></a>

### `SemanticChangeSets.merge`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.merge(self, left_id: str, right_id: str, name: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.merge`  
**Visibility:** public  
**Source line:** 30

<a id="function-semanticchangesets-conflicts"></a>

### `SemanticChangeSets.conflicts`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.conflicts(self, changeset_id: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.conflicts`  
**Visibility:** public  
**Source line:** 43

<a id="function-semanticchangesets-verify"></a>

### `SemanticChangeSets.verify`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.verify(self, changeset_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.verify`  
**Visibility:** public  
**Source line:** 44

<a id="function-semanticchangesets-rebase"></a>

### `SemanticChangeSets.rebase`

No function or method docstring is declared in the 0.7.5 source.

```python
def SemanticChangeSets.rebase(self, changeset_id: str, new_base_hash: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.rebase`  
**Visibility:** public  
**Source line:** 47

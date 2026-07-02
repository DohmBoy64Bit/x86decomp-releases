---
title: x86decomp.reconstruction.semantic_changesets
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-semantic-changesets.html
---

<a id="function-semanticchangesets-init"></a>
<a id="function-semanticchangesets-create"></a>
<a id="function-semanticchangesets-get"></a>
<a id="function-semanticchangesets-add-operation"></a>
<a id="function-semanticchangesets-merge"></a>
<a id="function-semanticchangesets-conflicts"></a>
<a id="function-semanticchangesets-verify"></a>
<a id="function-semanticchangesets-rebase"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.semantic_changesets

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 8 functions/methods

**Source:** `src/x86decomp/reconstruction/semantic_changesets.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `4342cc6206f76716dcc2007d36fd18ed0aff99cd7ebb562ef544adeeb8a537f3`.

## Functions and methods

Metadata: internal · line 9

### SemanticChangeSets.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.__init__`

Metadata: public · line 10

### SemanticChangeSets.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, name: str, *, base_audit_hash: str | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.create`

Metadata: public · line 15

### SemanticChangeSets.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, changeset_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.get`

Metadata: public · line 21

### SemanticChangeSets.add_operation

No function or method docstring is declared in the v0.7.4 source.

```
def add_operation(self, changeset_id: str, operation: dict[str, Any], *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.add_operation`

Metadata: public · line 30

### SemanticChangeSets.merge

No function or method docstring is declared in the v0.7.4 source.

```
def merge(self, left_id: str, right_id: str, name: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.merge`

Metadata: public · line 43

### SemanticChangeSets.conflicts

No function or method docstring is declared in the v0.7.4 source.

```
def conflicts(self, changeset_id: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.conflicts`

Metadata: public · line 44

### SemanticChangeSets.verify

No function or method docstring is declared in the v0.7.4 source.

```
def verify(self, changeset_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.verify`

Metadata: public · line 47

### SemanticChangeSets.rebase

No function or method docstring is declared in the v0.7.4 source.

```
def rebase(self, changeset_id: str, new_base_hash: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.semantic_changesets:SemanticChangeSets.rebase`

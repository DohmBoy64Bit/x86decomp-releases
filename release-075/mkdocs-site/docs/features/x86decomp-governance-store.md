---
title: x86decomp.governance.store
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.store`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/store.py`  
**SHA-256:** `495aab0ac7f4310b5af03783e96c35cf3f48acd6d8f26d92259cce51d5b85a31`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-governancestore-init"></a>

### `GovernanceStore.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def GovernanceStore.__init__(self, project_root: str | Path, *, database_path: str | Path | None=None)
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.__init__`  
**Visibility:** internal  
**Source line:** 296

<a id="function-governancestore-initialize"></a>

### `GovernanceStore.initialize`

No function or method docstring is declared in the 0.7.5 source.

```python
def GovernanceStore.initialize(self) -> None
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.initialize`  
**Visibility:** public  
**Source line:** 300

<a id="function-governancestore-connect"></a>

### `GovernanceStore.connect`

No function or method docstring is declared in the 0.7.5 source.

```python
def GovernanceStore.connect(self) -> sqlite3.Connection
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.connect`  
**Visibility:** public  
**Source line:** 318

<a id="function-governancestore-transaction"></a>

### `GovernanceStore.transaction`

No function or method docstring is declared in the 0.7.5 source.

```python
def GovernanceStore.transaction(self, *, immediate: bool=True) -> Iterator[sqlite3.Connection]
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.transaction`  
**Visibility:** public  
**Source line:** 328

<a id="function-governancestore-audit"></a>

### `GovernanceStore.audit`

No function or method docstring is declared in the 0.7.5 source.

```python
def GovernanceStore.audit(self, actor: str, category: str, subject_id: str | None, payload: dict[str, Any], *, connection: sqlite3.Connection | None=None) -> str
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.audit`  
**Visibility:** public  
**Source line:** 340

<a id="function-governancestore-verify-audit-chain"></a>

### `GovernanceStore.verify_audit_chain`

No function or method docstring is declared in the 0.7.5 source.

```python
def GovernanceStore.verify_audit_chain(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.verify_audit_chain`  
**Visibility:** public  
**Source line:** 375

<a id="function-governancestore-check"></a>

### `GovernanceStore.check`

No function or method docstring is declared in the 0.7.5 source.

```python
def GovernanceStore.check(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.check`  
**Visibility:** public  
**Source line:** 395

---
title: x86decomp.governance.candidates
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.candidates`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/candidates.py`  
**SHA-256:** `45b278d396b79ffecc4cfdd61e42af7e2cd5776f0b76f4f3a6b856283be0f1df`  
**Functions/methods:** 9

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-candidatestore-init"></a>

### `CandidateStore.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.__init__`  
**Visibility:** internal  
**Source line:** 15

<a id="function-candidatestore-create"></a>

### `CandidateStore.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.create(self, branch_name: str, *, campaign_id: str | None=None, parent_candidate_id: str | None=None, objective: dict[str, Any] | None=None, actor: str='system') -> str
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.create`  
**Visibility:** public  
**Source line:** 20

<a id="function-candidatestore-clone-files"></a>

### `CandidateStore._clone_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore._clone_files(self, parent_candidate_id: str, candidate_id: str, *, actor: str) -> None
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore._clone_files`  
**Visibility:** internal  
**Source line:** 37

<a id="function-candidatestore-add-file"></a>

### `CandidateStore.add_file`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.add_file(self, candidate_id: str, source: str | Path, relative_path: str | Path, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.add_file`  
**Visibility:** public  
**Source line:** 46

<a id="function-candidatestore-record-evaluation"></a>

### `CandidateStore.record_evaluation`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.record_evaluation(self, candidate_id: str, metric: str, status: str, *, value: float | None=None, details: dict[str, Any] | None=None, actor: str='validator') -> str
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.record_evaluation`  
**Visibility:** public  
**Source line:** 77

<a id="function-candidatestore-compare"></a>

### `CandidateStore.compare`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.compare(self, left_id: str, right_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.compare`  
**Visibility:** public  
**Source line:** 92

<a id="function-candidatestore-transition"></a>

### `CandidateStore.transition`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.transition(self, candidate_id: str, state: str, *, reason: str, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.transition`  
**Visibility:** public  
**Source line:** 114

<a id="function-candidatestore-get"></a>

### `CandidateStore.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.get(self, candidate_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.get`  
**Visibility:** public  
**Source line:** 138

<a id="function-candidatestore-list"></a>

### `CandidateStore.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def CandidateStore.list(self, *, campaign_id: str | None=None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.list`  
**Visibility:** public  
**Source line:** 153

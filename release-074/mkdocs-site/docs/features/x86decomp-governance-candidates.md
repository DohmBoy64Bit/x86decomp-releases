---
title: x86decomp.governance.candidates
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-candidates.html
---

<a id="function-candidatestore-init"></a>
<a id="function-candidatestore-create"></a>
<a id="function-candidatestore-clone-files"></a>
<a id="function-candidatestore-add-file"></a>
<a id="function-candidatestore-record-evaluation"></a>
<a id="function-candidatestore-compare"></a>
<a id="function-candidatestore-transition"></a>
<a id="function-candidatestore-get"></a>
<a id="function-candidatestore-list"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.candidates

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 9 functions/methods

**Source:** `src/x86decomp/governance/candidates.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `45b278d396b79ffecc4cfdd61e42af7e2cd5776f0b76f4f3a6b856283be0f1df`.

## Functions and methods

Metadata: internal · line 15

### CandidateStore.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.__init__`

Metadata: public · line 20

### CandidateStore.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, branch_name: str, *, campaign_id: str | None = None, parent_candidate_id: str | None = None, objective: dict[str, Any] | None = None, actor: str = 'system') -> str
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.create`

Metadata: internal · line 37

### CandidateStore._clone_files

No function or method docstring is declared in the v0.7.4 source.

```
def _clone_files(self, parent_candidate_id: str, candidate_id: str, *, actor: str) -> None
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore._clone_files`

Metadata: public · line 46

### CandidateStore.add_file

No function or method docstring is declared in the v0.7.4 source.

```
def add_file(self, candidate_id: str, source: str | Path, relative_path: str | Path, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.add_file`

Metadata: public · line 77

### CandidateStore.record_evaluation

No function or method docstring is declared in the v0.7.4 source.

```
def record_evaluation(self, candidate_id: str, metric: str, status: str, *, value: float | None = None, details: dict[str, Any] | None = None, actor: str = 'validator') -> str
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.record_evaluation`

Metadata: public · line 92

### CandidateStore.compare

No function or method docstring is declared in the v0.7.4 source.

```
def compare(self, left_id: str, right_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.compare`

Metadata: public · line 114

### CandidateStore.transition

No function or method docstring is declared in the v0.7.4 source.

```
def transition(self, candidate_id: str, state: str, *, reason: str, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.transition`

Metadata: public · line 138

### CandidateStore.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, candidate_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.get`

Metadata: public · line 153

### CandidateStore.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self, *, campaign_id: str | None = None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.candidates:CandidateStore.list`

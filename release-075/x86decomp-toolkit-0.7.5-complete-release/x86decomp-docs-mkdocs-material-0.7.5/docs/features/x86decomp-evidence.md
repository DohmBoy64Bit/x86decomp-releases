---
title: x86decomp.evidence
description: Evidence store and strict three-independent-source claim verification.
---

# `x86decomp.evidence`

Evidence store and strict three-independent-source claim verification.

**Area:** Toolkit  
**Source:** `src/x86decomp/evidence.py`  
**SHA-256:** `de8befd97c8e7f0529f7c3c2750836f8f38fab52e26987cf390d725faad3ee1e`  
**Functions/methods:** 12

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-validate-id"></a>

### `_validate_id`

No function or method docstring is declared in the 0.7.5 source.

```python
def _validate_id(value: str, field: str) -> None
```

**Catalog symbol:** `x86decomp.evidence:_validate_id`  
**Visibility:** internal  
**Source line:** 17

<a id="function-evidencestore-init"></a>

### `EvidenceStore.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.__init__(self, root: Path)
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.__init__`  
**Visibility:** internal  
**Source line:** 27

<a id="function-evidencestore-add-evidence"></a>

### `EvidenceStore.add_evidence`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.add_evidence(self, *, kind: EvidenceKind, source: str, locator: str, assertion: str, independent_group: str, file_path: Path | None=None, evidence_id: str | None=None, metadata: dict | None=None) -> EvidenceItem
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.add_evidence`  
**Visibility:** public  
**Source line:** 36

<a id="function-evidencestore-get-evidence"></a>

### `EvidenceStore.get_evidence`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.get_evidence(self, evidence_id: str) -> EvidenceItem
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.get_evidence`  
**Visibility:** public  
**Source line:** 81

<a id="function-evidencestore-create-claim"></a>

### `EvidenceStore.create_claim`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.create_claim(self, *, subject: str, predicate: str, object_value: str, evidence_ids: Iterable[str]=(), claim_id: str | None=None, notes: Iterable[str]=()) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.create_claim`  
**Visibility:** public  
**Source line:** 102

<a id="function-evidencestore-get-claim"></a>

### `EvidenceStore.get_claim`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.get_claim(self, claim_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.get_claim`  
**Visibility:** public  
**Source line:** 133

<a id="function-evidencestore-save-claim"></a>

### `EvidenceStore.save_claim`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.save_claim(self, claim: Claim) -> None
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.save_claim`  
**Visibility:** public  
**Source line:** 155

<a id="function-evidencestore-attach-evidence"></a>

### `EvidenceStore.attach_evidence`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.attach_evidence(self, claim_id: str, evidence_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.attach_evidence`  
**Visibility:** public  
**Source line:** 159

<a id="function-evidencestore-add-contradiction"></a>

### `EvidenceStore.add_contradiction`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.add_contradiction(self, claim_id: str, evidence_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.add_contradiction`  
**Visibility:** public  
**Source line:** 169

<a id="function-evidencestore-audit-evidence-integrity"></a>

### `EvidenceStore.audit_evidence_integrity`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.audit_evidence_integrity(self, item: EvidenceItem) -> list[str]
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.audit_evidence_integrity`  
**Visibility:** public  
**Source line:** 178

<a id="function-evidencestore-verify-claim"></a>

### `EvidenceStore.verify_claim`

Apply the strict verification gate and persist the resulting state.

VERIFIED requires all of the following:
- at least three evidence records;
- at least three independent groups;
- at least two evidence kinds;
- no contradiction records;
- every file-backed evidence hash still matches.

This is a governance rule, not a mathematical guarantee that a claim is true.

```python
def EvidenceStore.verify_claim(self, claim_id: str) -> dict
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.verify_claim`  
**Visibility:** public  
**Source line:** 200

<a id="function-evidencestore-require-verified"></a>

### `EvidenceStore.require_verified`

No function or method docstring is declared in the 0.7.5 source.

```python
def EvidenceStore.require_verified(self, claim_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.require_verified`  
**Visibility:** public  
**Source line:** 246

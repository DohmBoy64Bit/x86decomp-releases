---
title: x86decomp.evidence
description: Evidence store and strict three-independent-source claim verification.
original_path: features/x86decomp-evidence.html
---

<a id="function-validate-id"></a>
<a id="function-evidencestore-init"></a>
<a id="function-evidencestore-add-evidence"></a>
<a id="function-evidencestore-get-evidence"></a>
<a id="function-evidencestore-create-claim"></a>
<a id="function-evidencestore-get-claim"></a>
<a id="function-evidencestore-save-claim"></a>
<a id="function-evidencestore-attach-evidence"></a>
<a id="function-evidencestore-add-contradiction"></a>
<a id="function-evidencestore-audit-evidence-integrity"></a>
<a id="function-evidencestore-verify-claim"></a>
<a id="function-evidencestore-require-verified"></a>

Section: Source-derived feature and function reference

# x86decomp.evidence

Evidence store and strict three-independent-source claim verification.

Metadata: core · current · 12 functions/methods

**Source:** `src/x86decomp/evidence.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `de8befd97c8e7f0529f7c3c2750836f8f38fab52e26987cf390d725faad3ee1e`.

## Functions and methods

Metadata: internal · line 17

### _validate_id

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_id(value: str, field: str) -> None
```

**Catalog symbol:** `x86decomp.evidence:_validate_id`

Metadata: internal · line 27

### EvidenceStore.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, root: Path)
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.__init__`

Metadata: public · line 36

### EvidenceStore.add_evidence

No function or method docstring is declared in the v0.7.4 source.

```
def add_evidence(self, *, kind: EvidenceKind, source: str, locator: str, assertion: str, independent_group: str, file_path: Path | None = None, evidence_id: str | None = None, metadata: dict | None = None) -> EvidenceItem
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.add_evidence`

Metadata: public · line 81

### EvidenceStore.get_evidence

No function or method docstring is declared in the v0.7.4 source.

```
def get_evidence(self, evidence_id: str) -> EvidenceItem
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.get_evidence`

Metadata: public · line 102

### EvidenceStore.create_claim

No function or method docstring is declared in the v0.7.4 source.

```
def create_claim(self, *, subject: str, predicate: str, object_value: str, evidence_ids: Iterable[str] = (), claim_id: str | None = None, notes: Iterable[str] = ()) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.create_claim`

Metadata: public · line 133

### EvidenceStore.get_claim

No function or method docstring is declared in the v0.7.4 source.

```
def get_claim(self, claim_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.get_claim`

Metadata: public · line 155

### EvidenceStore.save_claim

No function or method docstring is declared in the v0.7.4 source.

```
def save_claim(self, claim: Claim) -> None
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.save_claim`

Metadata: public · line 159

### EvidenceStore.attach_evidence

No function or method docstring is declared in the v0.7.4 source.

```
def attach_evidence(self, claim_id: str, evidence_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.attach_evidence`

Metadata: public · line 169

### EvidenceStore.add_contradiction

No function or method docstring is declared in the v0.7.4 source.

```
def add_contradiction(self, claim_id: str, evidence_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.add_contradiction`

Metadata: public · line 178

### EvidenceStore.audit_evidence_integrity

No function or method docstring is declared in the v0.7.4 source.

```
def audit_evidence_integrity(self, item: EvidenceItem) -> list[str]
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.audit_evidence_integrity`

Metadata: public · line 200

### EvidenceStore.verify_claim

Apply the strict verification gate and persist the resulting state.

```
def verify_claim(self, claim_id: str) -> dict
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.verify_claim`

Metadata: public · line 246

### EvidenceStore.require_verified

No function or method docstring is declared in the v0.7.4 source.

```
def require_verified(self, claim_id: str) -> Claim
```

**Catalog symbol:** `x86decomp.evidence:EvidenceStore.require_verified`

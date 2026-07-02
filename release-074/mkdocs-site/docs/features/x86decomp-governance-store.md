---
title: x86decomp.governance.store
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-store.html
---

<a id="function-governancestore-init"></a>
<a id="function-governancestore-initialize"></a>
<a id="function-governancestore-connect"></a>
<a id="function-governancestore-transaction"></a>
<a id="function-governancestore-audit"></a>
<a id="function-governancestore-verify-audit-chain"></a>
<a id="function-governancestore-check"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.store

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 7 functions/methods

**Source:** `src/x86decomp/governance/store.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `548329cc6771568daa387a41ba8280ed8850391effbb9e450e41259909f862ae`.

## Functions and methods

Metadata: internal · line 296

### GovernanceStore.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, project_root: str | Path, *, database_path: str | Path | None = None)
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.__init__`

Metadata: public · line 300

### GovernanceStore.initialize

No function or method docstring is declared in the v0.7.4 source.

```
def initialize(self) -> None
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.initialize`

Metadata: public · line 318

### GovernanceStore.connect

No function or method docstring is declared in the v0.7.4 source.

```
def connect(self) -> sqlite3.Connection
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.connect`

Metadata: public · line 328

### GovernanceStore.transaction

No function or method docstring is declared in the v0.7.4 source.

```
def transaction(self, *, immediate: bool = True) -> Iterator[sqlite3.Connection]
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.transaction`

Metadata: public · line 340

### GovernanceStore.audit

No function or method docstring is declared in the v0.7.4 source.

```
def audit(self, actor: str, category: str, subject_id: str | None, payload: dict[str, Any], *, connection: sqlite3.Connection | None = None) -> str
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.audit`

Metadata: public · line 375

### GovernanceStore.verify_audit_chain

No function or method docstring is declared in the v0.7.4 source.

```
def verify_audit_chain(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.verify_audit_chain`

Metadata: public · line 395

### GovernanceStore.check

No function or method docstring is declared in the v0.7.4 source.

```
def check(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.store:GovernanceStore.check`

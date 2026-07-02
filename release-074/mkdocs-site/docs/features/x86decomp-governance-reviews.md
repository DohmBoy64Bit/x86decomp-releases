---
title: x86decomp.governance.reviews
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-reviews.html
---

<a id="function-reviewqueue-init"></a>
<a id="function-reviewqueue-create"></a>
<a id="function-reviewqueue-assign"></a>
<a id="function-reviewqueue-decide"></a>
<a id="function-reviewqueue-lock"></a>
<a id="function-reviewqueue-get"></a>
<a id="function-reviewqueue-list"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.reviews

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 7 functions/methods

**Source:** `src/x86decomp/governance/reviews.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `ba9d5d2757485bdcfdb2ed1255287013fe710def654fcbc2cf8a6801fe25312f`.

## Functions and methods

Metadata: internal · line 13

### ReviewQueue.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.__init__`

Metadata: public · line 17

### ReviewQueue.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, kind: str, subject_id: str, summary: str, *, priority: int = 50, details: dict[str, Any] | None = None, actor: str = 'system') -> str
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.create`

Metadata: public · line 30

### ReviewQueue.assign

No function or method docstring is declared in the v0.7.4 source.

```
def assign(self, review_id: str, assignee: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.assign`

Metadata: public · line 44

### ReviewQueue.decide

No function or method docstring is declared in the v0.7.4 source.

```
def decide(self, review_id: str, decision: str, rationale: str, *, actor: str = 'analyst', lock: bool = False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.decide`

Metadata: public · line 69

### ReviewQueue.lock

No function or method docstring is declared in the v0.7.4 source.

```
def lock(self, review_id: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.lock`

Metadata: public · line 78

### ReviewQueue.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, review_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.get`

Metadata: public · line 90

### ReviewQueue.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self, *, status: str | None = None, limit: int = 100) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.reviews:ReviewQueue.list`

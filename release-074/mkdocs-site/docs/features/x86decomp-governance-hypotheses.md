---
title: x86decomp.governance.hypotheses
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-hypotheses.html
---

<a id="function-row-to-hypothesis"></a>
<a id="function-hypothesisledger-init"></a>
<a id="function-hypothesisledger-create"></a>
<a id="function-hypothesisledger-get"></a>
<a id="function-hypothesisledger-list"></a>
<a id="function-hypothesisledger-add-dependency"></a>
<a id="function-hypothesisledger-has-dependency-cycle"></a>
<a id="function-hypothesisledger-attach-evidence"></a>
<a id="function-hypothesisledger-recalculate-confidence"></a>
<a id="function-hypothesisledger-transition"></a>
<a id="function-hypothesisledger-acceptance-gate"></a>
<a id="function-hypothesisledger-describe"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.hypotheses

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 12 functions/methods

**Source:** `src/x86decomp/governance/hypotheses.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `9b9601b00d885856a2311c6cf10fe62137eef992310ffd400cc0c84f7beff966`.

## Functions and methods

Metadata: internal · line 51

### _row_to_hypothesis

No function or method docstring is declared in the v0.7.4 source.

```
def _row_to_hypothesis(row: sqlite3.Row) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:_row_to_hypothesis`

Metadata: internal · line 68

### HypothesisLedger.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.__init__`

Metadata: public · line 72

### HypothesisLedger.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, statement: str, scope_kind: str, scope_id: str, *, origin: str, actor: str = 'system', hypothesis_id: str | None = None) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.create`

Metadata: public · line 94

### HypothesisLedger.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, hypothesis_id: str) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.get`

Metadata: public · line 101

### HypothesisLedger.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self, *, state: str | None = None, scope_id: str | None = None) -> list[Hypothesis]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.list`

Metadata: public · line 117

### HypothesisLedger.add_dependency

No function or method docstring is declared in the v0.7.4 source.

```
def add_dependency(self, hypothesis_id: str, depends_on_id: str, *, actor: str = 'system') -> None
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.add_dependency`

Metadata: internal · line 128

### HypothesisLedger._has_dependency_cycle

No function or method docstring is declared in the v0.7.4 source.

```
def _has_dependency_cycle(self, connection: sqlite3.Connection, start_id: str) -> bool
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger._has_dependency_cycle`

Metadata: public · line 139

### HypothesisLedger.attach_evidence

No function or method docstring is declared in the v0.7.4 source.

```
def attach_evidence(self, hypothesis_id: str, evidence_id: str, *, stance: str, weight: float, evidence_kind: str, independence_group: str, artifact_sha256: str | None = None, details: dict[str, Any] | None = None, actor: str = 'system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.attach_evidence`

Metadata: internal · line 169

### HypothesisLedger._recalculate_confidence

No function or method docstring is declared in the v0.7.4 source.

```
def _recalculate_confidence(self, connection: sqlite3.Connection, hypothesis_id: str) -> float
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger._recalculate_confidence`

Metadata: public · line 186

### HypothesisLedger.transition

No function or method docstring is declared in the v0.7.4 source.

```
def transition(self, hypothesis_id: str, new_state: str, *, reason: str, actor: str = 'analyst', lock: bool | None = None) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.transition`

Metadata: public · line 208

### HypothesisLedger.acceptance_gate

No function or method docstring is declared in the v0.7.4 source.

```
def acceptance_gate(self, hypothesis_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.acceptance_gate`

Metadata: public · line 241

### HypothesisLedger.describe

No function or method docstring is declared in the v0.7.4 source.

```
def describe(self, hypothesis_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.describe`

---
title: x86decomp.governance.hypotheses
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.hypotheses`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/hypotheses.py`  
**SHA-256:** `9b9601b00d885856a2311c6cf10fe62137eef992310ffd400cc0c84f7beff966`  
**Functions/methods:** 12

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-row-to-hypothesis"></a>

### `_row_to_hypothesis`

No function or method docstring is declared in the 0.7.5 source.

```python
def _row_to_hypothesis(row: sqlite3.Row) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:_row_to_hypothesis`  
**Visibility:** internal  
**Source line:** 51

<a id="function-hypothesisledger-init"></a>

### `HypothesisLedger.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.__init__`  
**Visibility:** internal  
**Source line:** 68

<a id="function-hypothesisledger-create"></a>

### `HypothesisLedger.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.create(self, statement: str, scope_kind: str, scope_id: str, *, origin: str, actor: str='system', hypothesis_id: str | None=None) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.create`  
**Visibility:** public  
**Source line:** 72

<a id="function-hypothesisledger-get"></a>

### `HypothesisLedger.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.get(self, hypothesis_id: str) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.get`  
**Visibility:** public  
**Source line:** 94

<a id="function-hypothesisledger-list"></a>

### `HypothesisLedger.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.list(self, *, state: str | None=None, scope_id: str | None=None) -> list[Hypothesis]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.list`  
**Visibility:** public  
**Source line:** 101

<a id="function-hypothesisledger-add-dependency"></a>

### `HypothesisLedger.add_dependency`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.add_dependency(self, hypothesis_id: str, depends_on_id: str, *, actor: str='system') -> None
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.add_dependency`  
**Visibility:** public  
**Source line:** 117

<a id="function-hypothesisledger-has-dependency-cycle"></a>

### `HypothesisLedger._has_dependency_cycle`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger._has_dependency_cycle(self, connection: sqlite3.Connection, start_id: str) -> bool
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger._has_dependency_cycle`  
**Visibility:** internal  
**Source line:** 128

<a id="function-hypothesisledger-attach-evidence"></a>

### `HypothesisLedger.attach_evidence`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.attach_evidence(self, hypothesis_id: str, evidence_id: str, *, stance: str, weight: float, evidence_kind: str, independence_group: str, artifact_sha256: str | None=None, details: dict[str, Any] | None=None, actor: str='system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.attach_evidence`  
**Visibility:** public  
**Source line:** 139

<a id="function-hypothesisledger-recalculate-confidence"></a>

### `HypothesisLedger._recalculate_confidence`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger._recalculate_confidence(self, connection: sqlite3.Connection, hypothesis_id: str) -> float
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger._recalculate_confidence`  
**Visibility:** internal  
**Source line:** 169

<a id="function-hypothesisledger-transition"></a>

### `HypothesisLedger.transition`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.transition(self, hypothesis_id: str, new_state: str, *, reason: str, actor: str='analyst', lock: bool | None=None) -> Hypothesis
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.transition`  
**Visibility:** public  
**Source line:** 186

<a id="function-hypothesisledger-acceptance-gate"></a>

### `HypothesisLedger.acceptance_gate`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.acceptance_gate(self, hypothesis_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.acceptance_gate`  
**Visibility:** public  
**Source line:** 208

<a id="function-hypothesisledger-describe"></a>

### `HypothesisLedger.describe`

No function or method docstring is declared in the 0.7.5 source.

```python
def HypothesisLedger.describe(self, hypothesis_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.hypotheses:HypothesisLedger.describe`  
**Visibility:** public  
**Source line:** 241

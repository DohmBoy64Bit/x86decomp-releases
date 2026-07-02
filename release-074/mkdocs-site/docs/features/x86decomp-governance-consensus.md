---
title: x86decomp.governance.consensus
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-consensus.html
---

<a id="function-consensusengine-init"></a>
<a id="function-consensusengine-record"></a>
<a id="function-consensusengine-scan"></a>
<a id="function-consensusengine-conflicts"></a>
<a id="function-consensusengine-resolve"></a>
<a id="function-consensusengine-explain"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.consensus

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 6 functions/methods

**Source:** `src/x86decomp/governance/consensus.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `41c250face5e2cb3dd5a56c6e741d5cbebdc25e6e9f1531a25181d9d944a5eb3`.

## Functions and methods

Metadata: internal · line 12

### ConsensusEngine.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.__init__`

Metadata: public · line 16

### ConsensusEngine.record

No function or method docstring is declared in the v0.7.4 source.

```
def record(self, subject_kind: str, subject_id: str, property_name: str, value: Any, *, adapter_name: str, adapter_version: str, evidence_id: str, independence_group: str, confidence: float = 1.0, actor: str = 'adapter') -> str
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.record`

Metadata: public · line 28

### ConsensusEngine.scan

No function or method docstring is declared in the v0.7.4 source.

```
def scan(self, *, subject_kind: str | None = None, subject_id: str | None = None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.scan`

Metadata: public · line 70

### ConsensusEngine.conflicts

No function or method docstring is declared in the v0.7.4 source.

```
def conflicts(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.conflicts`

Metadata: public · line 73

### ConsensusEngine.resolve

No function or method docstring is declared in the v0.7.4 source.

```
def resolve(self, subject_kind: str, subject_id: str, property_name: str, selected_value: Any, *, method: str, rationale: str, actor: str = 'analyst', lock: bool = False) -> str
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.resolve`

Metadata: public · line 94

### ConsensusEngine.explain

No function or method docstring is declared in the v0.7.4 source.

```
def explain(self, subject_kind: str, subject_id: str, property_name: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.explain`

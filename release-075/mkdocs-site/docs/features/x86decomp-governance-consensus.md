---
title: x86decomp.governance.consensus
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.consensus`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/consensus.py`  
**SHA-256:** `41c250face5e2cb3dd5a56c6e741d5cbebdc25e6e9f1531a25181d9d944a5eb3`  
**Functions/methods:** 6

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-consensusengine-init"></a>

### `ConsensusEngine.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ConsensusEngine.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.__init__`  
**Visibility:** internal  
**Source line:** 12

<a id="function-consensusengine-record"></a>

### `ConsensusEngine.record`

No function or method docstring is declared in the 0.7.5 source.

```python
def ConsensusEngine.record(self, subject_kind: str, subject_id: str, property_name: str, value: Any, *, adapter_name: str, adapter_version: str, evidence_id: str, independence_group: str, confidence: float=1.0, actor: str='adapter') -> str
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.record`  
**Visibility:** public  
**Source line:** 16

<a id="function-consensusengine-scan"></a>

### `ConsensusEngine.scan`

No function or method docstring is declared in the 0.7.5 source.

```python
def ConsensusEngine.scan(self, *, subject_kind: str | None=None, subject_id: str | None=None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.scan`  
**Visibility:** public  
**Source line:** 28

<a id="function-consensusengine-conflicts"></a>

### `ConsensusEngine.conflicts`

No function or method docstring is declared in the 0.7.5 source.

```python
def ConsensusEngine.conflicts(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.conflicts`  
**Visibility:** public  
**Source line:** 70

<a id="function-consensusengine-resolve"></a>

### `ConsensusEngine.resolve`

No function or method docstring is declared in the 0.7.5 source.

```python
def ConsensusEngine.resolve(self, subject_kind: str, subject_id: str, property_name: str, selected_value: Any, *, method: str, rationale: str, actor: str='analyst', lock: bool=False) -> str
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.resolve`  
**Visibility:** public  
**Source line:** 73

<a id="function-consensusengine-explain"></a>

### `ConsensusEngine.explain`

No function or method docstring is declared in the 0.7.5 source.

```python
def ConsensusEngine.explain(self, subject_kind: str, subject_id: str, property_name: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.consensus:ConsensusEngine.explain`  
**Visibility:** public  
**Source line:** 94

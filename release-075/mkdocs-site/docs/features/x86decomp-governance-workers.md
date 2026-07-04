---
title: x86decomp.governance.workers
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.workers`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/workers.py`  
**SHA-256:** `4538ea72a7fe80900916a18a6bbba5ac7a3617d1765b1b981691ebad10f4e656`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-workerregistry-init"></a>

### `WorkerRegistry.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerRegistry.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.__init__`  
**Visibility:** internal  
**Source line:** 13

<a id="function-workerregistry-register"></a>

### `WorkerRegistry.register`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerRegistry.register(self, name: str, capabilities: dict[str, Any], *, endpoint: str | None=None, environment_sha256: str | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.register`  
**Visibility:** public  
**Source line:** 17

<a id="function-workerregistry-get"></a>

### `WorkerRegistry.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerRegistry.get(self, worker_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.get`  
**Visibility:** public  
**Source line:** 31

<a id="function-workerregistry-list"></a>

### `WorkerRegistry.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerRegistry.list(self, *, status: str | None=None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.list`  
**Visibility:** public  
**Source line:** 40

<a id="function-workerregistry-select"></a>

### `WorkerRegistry.select`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerRegistry.select(self, required: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.select`  
**Visibility:** public  
**Source line:** 48

<a id="function-workerregistry-set-status"></a>

### `WorkerRegistry.set_status`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerRegistry.set_status(self, worker_id: str, status: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.set_status`  
**Visibility:** public  
**Source line:** 58

<a id="function-workerregistry-doctor"></a>

### `WorkerRegistry.doctor`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerRegistry.doctor(self, worker_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.doctor`  
**Visibility:** public  
**Source line:** 67

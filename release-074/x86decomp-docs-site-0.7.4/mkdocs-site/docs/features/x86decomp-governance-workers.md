---
title: x86decomp.governance.workers
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-workers.html
---

<a id="function-workerregistry-init"></a>
<a id="function-workerregistry-register"></a>
<a id="function-workerregistry-get"></a>
<a id="function-workerregistry-list"></a>
<a id="function-workerregistry-select"></a>
<a id="function-workerregistry-set-status"></a>
<a id="function-workerregistry-doctor"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.workers

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 7 functions/methods

**Source:** `src/x86decomp/governance/workers.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `4538ea72a7fe80900916a18a6bbba5ac7a3617d1765b1b981691ebad10f4e656`.

## Functions and methods

Metadata: internal · line 13

### WorkerRegistry.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.__init__`

Metadata: public · line 17

### WorkerRegistry.register

No function or method docstring is declared in the v0.7.4 source.

```
def register(self, name: str, capabilities: dict[str, Any], *, endpoint: str | None = None, environment_sha256: str | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.register`

Metadata: public · line 31

### WorkerRegistry.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, worker_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.get`

Metadata: public · line 40

### WorkerRegistry.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self, *, status: str | None = None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.list`

Metadata: public · line 48

### WorkerRegistry.select

No function or method docstring is declared in the v0.7.4 source.

```
def select(self, required: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.select`

Metadata: public · line 58

### WorkerRegistry.set_status

No function or method docstring is declared in the v0.7.4 source.

```
def set_status(self, worker_id: str, status: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.set_status`

Metadata: public · line 67

### WorkerRegistry.doctor

No function or method docstring is declared in the v0.7.4 source.

```
def doctor(self, worker_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.workers:WorkerRegistry.doctor`

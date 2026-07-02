---
title: x86decomp.work_queue
description: Evidence-gated human/AI work queue with validator acceptance rules.
original_path: features/x86decomp-work-queue.html
---

<a id="function-workqueue-init"></a>
<a id="function-workqueue-close"></a>
<a id="function-workqueue-create"></a>
<a id="function-workqueue-get"></a>
<a id="function-workqueue-claim"></a>
<a id="function-workqueue-propose"></a>
<a id="function-workqueue-record-validator"></a>
<a id="function-workqueue-next"></a>

Section: Source-derived feature and function reference

# x86decomp.work_queue

Evidence-gated human/AI work queue with validator acceptance rules.

Metadata: core · current · 8 functions/methods

**Source:** `src/x86decomp/work_queue.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `b1392399ca7536f6f1c1a78b16b62b61f7b70a744d2a529860e03d3371377c6e`.

## Functions and methods

Metadata: internal · line 36

### WorkQueue.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, path: Path)
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.__init__`

Metadata: public · line 43

### WorkQueue.close

No function or method docstring is declared in the v0.7.4 source.

```
def close(self) -> None
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.close`

Metadata: public · line 46

### WorkQueue.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, *, function_id: str, mode: str, kind: str, instructions: str, required_validators: list[str], priority: int = 0) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.create`

Metadata: public · line 69

### WorkQueue.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, task_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.get`

Metadata: public · line 79

### WorkQueue.claim

No function or method docstring is declared in the v0.7.4 source.

```
def claim(self, task_id: str, assignee: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.claim`

Metadata: public · line 88

### WorkQueue.propose

No function or method docstring is declared in the v0.7.4 source.

```
def propose(self, task_id: str, proposal: dict[str, Any], evidence_ids: list[str]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.propose`

Metadata: public · line 100

### WorkQueue.record_validator

No function or method docstring is declared in the v0.7.4 source.

```
def record_validator(self, task_id: str, validator: str, report_path: str, passed: bool) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.record_validator`

Metadata: public · line 114

### WorkQueue.next

No function or method docstring is declared in the v0.7.4 source.

```
def next(self, *, mode: str | None = None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.next`

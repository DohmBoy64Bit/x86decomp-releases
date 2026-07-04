---
title: x86decomp.work_queue
description: Evidence-gated human/AI work queue with validator acceptance rules.
---

# `x86decomp.work_queue`

Evidence-gated human/AI work queue with validator acceptance rules.

**Area:** Toolkit  
**Source:** `src/x86decomp/work_queue.py`  
**SHA-256:** `b1392399ca7536f6f1c1a78b16b62b61f7b70a744d2a529860e03d3371377c6e`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-workqueue-init"></a>

### `WorkQueue.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.__init__(self, path: Path)
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.__init__`  
**Visibility:** internal  
**Source line:** 36

<a id="function-workqueue-close"></a>

### `WorkQueue.close`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.close(self) -> None
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.close`  
**Visibility:** public  
**Source line:** 43

<a id="function-workqueue-create"></a>

### `WorkQueue.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.create(self, *, function_id: str, mode: str, kind: str, instructions: str, required_validators: list[str], priority: int=0) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.create`  
**Visibility:** public  
**Source line:** 46

<a id="function-workqueue-get"></a>

### `WorkQueue.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.get(self, task_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.get`  
**Visibility:** public  
**Source line:** 69

<a id="function-workqueue-claim"></a>

### `WorkQueue.claim`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.claim(self, task_id: str, assignee: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.claim`  
**Visibility:** public  
**Source line:** 79

<a id="function-workqueue-propose"></a>

### `WorkQueue.propose`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.propose(self, task_id: str, proposal: dict[str, Any], evidence_ids: list[str]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.propose`  
**Visibility:** public  
**Source line:** 88

<a id="function-workqueue-record-validator"></a>

### `WorkQueue.record_validator`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.record_validator(self, task_id: str, validator: str, report_path: str, passed: bool) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.record_validator`  
**Visibility:** public  
**Source line:** 100

<a id="function-workqueue-next"></a>

### `WorkQueue.next`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkQueue.next(self, *, mode: str | None=None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.work_queue:WorkQueue.next`  
**Visibility:** public  
**Source line:** 114

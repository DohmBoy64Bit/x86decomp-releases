---
title: x86decomp.orchestrator
description: Durable, resumable pipeline orchestration.
---

# `x86decomp.orchestrator`

Durable, resumable pipeline orchestration.

Pipeline stages are concrete command executions or explicit evidence gates.  A
stage is never represented by an unimplemented placeholder.  Missing tools or
unmet evidence produce a durable BLOCKED state with an actionable reason.

**Area:** Toolkit  
**Source:** `src/x86decomp/orchestrator.py`  
**SHA-256:** `752a6e6b5d4f931007e93ee7898f6a0d2500b044266c7153a27be7e7eb49477e`  
**Functions/methods:** 22

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-pipelinestage-from-dict"></a>

### `PipelineStage.from_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def PipelineStage.from_dict(cls, value: Any) -> 'PipelineStage'
```

**Catalog symbol:** `x86decomp.orchestrator:PipelineStage.from_dict`  
**Visibility:** public  
**Source line:** 100

<a id="function-pipelinemanifest-load"></a>

### `PipelineManifest.load`

No function or method docstring is declared in the 0.7.5 source.

```python
def PipelineManifest.load(cls, path: Path) -> 'PipelineManifest'
```

**Catalog symbol:** `x86decomp.orchestrator:PipelineManifest.load`  
**Visibility:** public  
**Source line:** 159

<a id="function-orchestrator-init"></a>

### `Orchestrator.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.__init__(self, project_root: Path)
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.__init__`  
**Visibility:** internal  
**Source line:** 188

<a id="function-orchestrator-close"></a>

### `Orchestrator.close`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.close(self) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.close`  
**Visibility:** public  
**Source line:** 218

<a id="function-orchestrator-enter"></a>

### `Orchestrator.__enter__`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.__enter__(self) -> 'Orchestrator'
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.__enter__`  
**Visibility:** internal  
**Source line:** 221

<a id="function-orchestrator-exit"></a>

### `Orchestrator.__exit__`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.__exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.__exit__`  
**Visibility:** internal  
**Source line:** 224

<a id="function-orchestrator-transaction"></a>

### `Orchestrator._transaction`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._transaction(self) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._transaction`  
**Visibility:** internal  
**Source line:** 227

<a id="function-orchestrator-register"></a>

### `Orchestrator.register`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.register(self, manifest_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.register`  
**Visibility:** public  
**Source line:** 230

<a id="function-orchestrator-idempotency-key"></a>

### `Orchestrator._idempotency_key`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._idempotency_key(self, stage: PipelineStage) -> str
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._idempotency_key`  
**Visibility:** internal  
**Source line:** 271

<a id="function-orchestrator-event"></a>

### `Orchestrator._event`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._event(self, job_id: str, event: str, details: dict[str, Any]) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._event`  
**Visibility:** internal  
**Source line:** 295

<a id="function-orchestrator-completed-result-is-intact"></a>

### `Orchestrator._completed_result_is_intact`

Verify materialized outputs before reusing a succeeded job.

```python
def Orchestrator._completed_result_is_intact(self, row: sqlite3.Row) -> bool
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._completed_result_is_intact`  
**Visibility:** internal  
**Source line:** 301

<a id="function-orchestrator-materialize-outputs"></a>

### `Orchestrator._materialize_outputs`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._materialize_outputs(self, pipeline_id: str, stage: PipelineStage, job_id: str, work: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._materialize_outputs`  
**Visibility:** internal  
**Source line:** 326

<a id="function-orchestrator-dependency-states"></a>

### `Orchestrator._dependency_states`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._dependency_states(self, pipeline_id: str, dependencies: Iterable[str]) -> dict[str, str]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._dependency_states`  
**Visibility:** internal  
**Source line:** 360

<a id="function-orchestrator-run"></a>

### `Orchestrator.run`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.run(self, manifest_path: Path, *, stop_on_failure: bool=True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.run`  
**Visibility:** public  
**Source line:** 370

<a id="function-orchestrator-set-state"></a>

### `Orchestrator._set_state`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._set_state(self, job_id: str, state: JobState, *, result: dict[str, Any] | None=None, error: str | None=None) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._set_state`  
**Visibility:** internal  
**Source line:** 402

<a id="function-orchestrator-run-stage"></a>

### `Orchestrator._run_stage`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._run_stage(self, manifest: PipelineManifest, stage: PipelineStage, job_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._run_stage`  
**Visibility:** internal  
**Source line:** 417

<a id="function-orchestrator-recover-stale-jobs"></a>

### `Orchestrator.recover_stale_jobs`

Reset only RUNNING jobs whose durable heartbeat is older than the bound.

```python
def Orchestrator.recover_stale_jobs(self, *, pipeline_id: str | None=None, stale_seconds: int=600) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.recover_stale_jobs`  
**Visibility:** public  
**Source line:** 526

<a id="function-orchestrator-cancel"></a>

### `Orchestrator.cancel`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.cancel(self, pipeline_id: str, stage_id: str | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.cancel`  
**Visibility:** public  
**Source line:** 571

<a id="function-orchestrator-retry"></a>

### `Orchestrator.retry`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.retry(self, pipeline_id: str, stage_id: str, *, cascade: bool=False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.retry`  
**Visibility:** public  
**Source line:** 590

<a id="function-orchestrator-update-pipeline-status"></a>

### `Orchestrator._update_pipeline_status`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator._update_pipeline_status(self, pipeline_id: str) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._update_pipeline_status`  
**Visibility:** internal  
**Source line:** 615

<a id="function-orchestrator-status"></a>

### `Orchestrator.status`

No function or method docstring is declared in the 0.7.5 source.

```python
def Orchestrator.status(self, pipeline_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.status`  
**Visibility:** public  
**Source line:** 631

<a id="function-create-default-pipeline"></a>

### `create_default_pipeline`

Generate a concrete pipeline for the current project.

The generated stages invoke real toolkit commands.  Ghidra is included only
when requested and becomes BLOCKED at runtime if its configured executable
is unavailable; no fake analysis output is generated.

```python
def create_default_pipeline(project_root: Path, output: Path, *, include_ghidra: bool=True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:create_default_pipeline`  
**Visibility:** public  
**Source line:** 662

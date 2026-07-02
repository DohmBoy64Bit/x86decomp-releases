---
title: x86decomp.orchestrator
description: Durable, resumable pipeline orchestration.
original_path: features/x86decomp-orchestrator.html
---

<a id="function-pipelinestage-from-dict"></a>
<a id="function-pipelinemanifest-load"></a>
<a id="function-orchestrator-init"></a>
<a id="function-orchestrator-close"></a>
<a id="function-orchestrator-enter"></a>
<a id="function-orchestrator-exit"></a>
<a id="function-orchestrator-transaction"></a>
<a id="function-orchestrator-register"></a>
<a id="function-orchestrator-idempotency-key"></a>
<a id="function-orchestrator-event"></a>
<a id="function-orchestrator-completed-result-is-intact"></a>
<a id="function-orchestrator-materialize-outputs"></a>
<a id="function-orchestrator-dependency-states"></a>
<a id="function-orchestrator-run"></a>
<a id="function-orchestrator-set-state"></a>
<a id="function-orchestrator-run-stage"></a>
<a id="function-orchestrator-recover-stale-jobs"></a>
<a id="function-orchestrator-cancel"></a>
<a id="function-orchestrator-retry"></a>
<a id="function-orchestrator-update-pipeline-status"></a>
<a id="function-orchestrator-status"></a>
<a id="function-create-default-pipeline"></a>

Section: Source-derived feature and function reference

# x86decomp.orchestrator

Durable, resumable pipeline orchestration.

Metadata: core · current · 22 functions/methods

**Source:** `src/x86decomp/orchestrator.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `752a6e6b5d4f931007e93ee7898f6a0d2500b044266c7153a27be7e7eb49477e`.

## Functions and methods

Metadata: public · line 100

### PipelineStage.from_dict

No function or method docstring is declared in the v0.7.4 source.

```
def from_dict(cls, value: Any) -> 'PipelineStage'
```

**Catalog symbol:** `x86decomp.orchestrator:PipelineStage.from_dict`

Metadata: public · line 159

### PipelineManifest.load

No function or method docstring is declared in the v0.7.4 source.

```
def load(cls, path: Path) -> 'PipelineManifest'
```

**Catalog symbol:** `x86decomp.orchestrator:PipelineManifest.load`

Metadata: internal · line 188

### Orchestrator.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, project_root: Path)
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.__init__`

Metadata: public · line 218

### Orchestrator.close

No function or method docstring is declared in the v0.7.4 source.

```
def close(self) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.close`

Metadata: internal · line 221

### Orchestrator.__enter__

No function or method docstring is declared in the v0.7.4 source.

```
def __enter__(self) -> 'Orchestrator'
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.__enter__`

Metadata: internal · line 224

### Orchestrator.__exit__

No function or method docstring is declared in the v0.7.4 source.

```
def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.__exit__`

Metadata: internal · line 227

### Orchestrator._transaction

No function or method docstring is declared in the v0.7.4 source.

```
def _transaction(self) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._transaction`

Metadata: public · line 230

### Orchestrator.register

No function or method docstring is declared in the v0.7.4 source.

```
def register(self, manifest_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.register`

Metadata: internal · line 271

### Orchestrator._idempotency_key

No function or method docstring is declared in the v0.7.4 source.

```
def _idempotency_key(self, stage: PipelineStage) -> str
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._idempotency_key`

Metadata: internal · line 295

### Orchestrator._event

No function or method docstring is declared in the v0.7.4 source.

```
def _event(self, job_id: str, event: str, details: dict[str, Any]) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._event`

Metadata: internal · line 301

### Orchestrator._completed_result_is_intact

Verify materialized outputs before reusing a succeeded job.

```
def _completed_result_is_intact(self, row: sqlite3.Row) -> bool
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._completed_result_is_intact`

Metadata: internal · line 326

### Orchestrator._materialize_outputs

No function or method docstring is declared in the v0.7.4 source.

```
def _materialize_outputs(self, pipeline_id: str, stage: PipelineStage, job_id: str, work: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._materialize_outputs`

Metadata: internal · line 360

### Orchestrator._dependency_states

No function or method docstring is declared in the v0.7.4 source.

```
def _dependency_states(self, pipeline_id: str, dependencies: Iterable[str]) -> dict[str, str]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._dependency_states`

Metadata: public · line 370

### Orchestrator.run

No function or method docstring is declared in the v0.7.4 source.

```
def run(self, manifest_path: Path, *, stop_on_failure: bool = True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.run`

Metadata: internal · line 402

### Orchestrator._set_state

No function or method docstring is declared in the v0.7.4 source.

```
def _set_state(self, job_id: str, state: JobState, *, result: dict[str, Any] | None = None, error: str | None = None) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._set_state`

Metadata: internal · line 417

### Orchestrator._run_stage

No function or method docstring is declared in the v0.7.4 source.

```
def _run_stage(self, manifest: PipelineManifest, stage: PipelineStage, job_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._run_stage`

Metadata: public · line 526

### Orchestrator.recover_stale_jobs

Reset only RUNNING jobs whose durable heartbeat is older than the bound.

```
def recover_stale_jobs(self, *, pipeline_id: str | None = None, stale_seconds: int = 600) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.recover_stale_jobs`

Metadata: public · line 571

### Orchestrator.cancel

No function or method docstring is declared in the v0.7.4 source.

```
def cancel(self, pipeline_id: str, stage_id: str | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.cancel`

Metadata: public · line 590

### Orchestrator.retry

No function or method docstring is declared in the v0.7.4 source.

```
def retry(self, pipeline_id: str, stage_id: str, *, cascade: bool = False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.retry`

Metadata: internal · line 615

### Orchestrator._update_pipeline_status

No function or method docstring is declared in the v0.7.4 source.

```
def _update_pipeline_status(self, pipeline_id: str) -> None
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator._update_pipeline_status`

Metadata: public · line 631

### Orchestrator.status

No function or method docstring is declared in the v0.7.4 source.

```
def status(self, pipeline_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:Orchestrator.status`

Metadata: public · line 662

### create_default_pipeline

Generate a concrete pipeline for the current project.

```
def create_default_pipeline(project_root: Path, output: Path, *, include_ghidra: bool = True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.orchestrator:create_default_pipeline`

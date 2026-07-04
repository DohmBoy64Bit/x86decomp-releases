---
title: x86decomp.orchestrator
description: Source module reference for x86decomp.orchestrator.
---

# `x86decomp.orchestrator`

**Source path:** `src/x86decomp/orchestrator.py`  
**Documented symbols:** 28

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `JobState` | class | 32 | 38 | — |
| `PipelineStage` | class | 86 | 149 | — |
| `from_dict` | function | 100 | 149 | — |
| `strings` | function | 109 | 113 | — |
| `PipelineManifest` | class | 153 | 184 | — |
| `load` | function | 159 | 184 | — |
| `Orchestrator` | class | 187 | 659 | — |
| `__init__` | function | 188 | 216 | — |
| `close` | function | 218 | 219 | — |
| `__enter__` | function | 221 | 222 | — |
| `__exit__` | function | 224 | 225 | — |
| `_transaction` | function | 227 | 228 | — |
| `register` | function | 230 | 269 | — |
| `_idempotency_key` | function | 271 | 293 | — |
| `_event` | function | 295 | 299 | — |
| `_completed_result_is_intact` | function | 301 | 324 | Verify materialized outputs before reusing a succeeded job. |
| `_materialize_outputs` | function | 326 | 358 | — |
| `_dependency_states` | function | 360 | 368 | — |
| `run` | function | 370 | 400 | — |
| `_set_state` | function | 402 | 415 | — |
| `_run_stage` | function | 417 | 524 | — |
| `cancellation_requested` | function | 495 | 504 | — |
| `recover_stale_jobs` | function | 526 | 569 | Reset only RUNNING jobs whose durable heartbeat is older than the bound. |
| `cancel` | function | 571 | 588 | — |
| `retry` | function | 590 | 613 | — |
| `_update_pipeline_status` | function | 615 | 629 | — |
| `status` | function | 631 | 659 | — |
| `create_default_pipeline` | function | 662 | 743 | Generate a concrete pipeline for the current project. |

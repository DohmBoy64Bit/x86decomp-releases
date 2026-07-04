---
title: x86decomp.orchestrator
description: Source module reference for x86decomp.orchestrator.
---

# `x86decomp.orchestrator`

**Source path:** `src/x86decomp/orchestrator.py`  
**SHA-256:** `752a6e6b5d4f931007e93ee7898f6a0d2500b044266c7153a27be7e7eb49477e`  
**Documented symbols:** 28

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `JobState` | class | 32 | 38 | no docstring declared |
| `PipelineStage` | class | 86 | 149 | no docstring declared |
| `from_dict` | function | 100 | 149 | no docstring declared |
| `strings` | function | 109 | 113 | no docstring declared |
| `PipelineManifest` | class | 153 | 184 | no docstring declared |
| `load` | function | 159 | 184 | no docstring declared |
| `Orchestrator` | class | 187 | 659 | no docstring declared |
| `__init__` | function | 188 | 216 | no docstring declared |
| `close` | function | 218 | 219 | no docstring declared |
| `__enter__` | function | 221 | 222 | no docstring declared |
| `__exit__` | function | 224 | 225 | no docstring declared |
| `_transaction` | function | 227 | 228 | no docstring declared |
| `register` | function | 230 | 269 | no docstring declared |
| `_idempotency_key` | function | 271 | 293 | no docstring declared |
| `_event` | function | 295 | 299 | no docstring declared |
| `_completed_result_is_intact` | function | 301 | 324 | Verify materialized outputs before reusing a succeeded job. |
| `_materialize_outputs` | function | 326 | 358 | no docstring declared |
| `_dependency_states` | function | 360 | 368 | no docstring declared |
| `run` | function | 370 | 400 | no docstring declared |
| `_set_state` | function | 402 | 415 | no docstring declared |
| `_run_stage` | function | 417 | 524 | no docstring declared |
| `cancellation_requested` | function | 495 | 504 | no docstring declared |
| `recover_stale_jobs` | function | 526 | 569 | Reset only RUNNING jobs whose durable heartbeat is older than the bound. |
| `cancel` | function | 571 | 588 | no docstring declared |
| `retry` | function | 590 | 613 | no docstring declared |
| `_update_pipeline_status` | function | 615 | 629 | no docstring declared |
| `status` | function | 631 | 659 | no docstring declared |
| `create_default_pipeline` | function | 662 | 743 | Generate a concrete pipeline for the current project. |

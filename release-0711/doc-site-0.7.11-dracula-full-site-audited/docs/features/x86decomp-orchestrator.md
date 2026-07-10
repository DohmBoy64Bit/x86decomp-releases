---
title: x86decomp.orchestrator
description: Module reference for x86decomp.orchestrator.
---

# `x86decomp.orchestrator`

- Area: `toolkit`
- Source path: `src/x86decomp/orchestrator.py`
- SHA-256: `fab775aab1d71a2fa1a728147b8792302350689496896caa3a1936a502dbdfd7`
- Size: `35886` bytes
- Lines: `769`

## Module docstring

Durable, resumable pipeline orchestration.

Pipeline stages are concrete command executions or explicit evidence gates.  A
stage is never represented by an unimplemented placeholder.  Missing tools or
unmet evidence produce a durable BLOCKED state with an actionable reason.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `JobState` | 32 | Coordinate job state behavior for the current toolkit workflow. |
| class | `PipelineStage` | 87 | Store validated pipeline stage fields used by toolkit reports and adapters. |
| function | `from_dict` | 102 | Execute the from dict operation for the current toolkit workflow. |
| function | `strings` | 112 | Execute the strings operation for the current toolkit workflow. |
| class | `PipelineManifest` | 157 | Store validated pipeline manifest fields used by toolkit reports and adapters. |
| function | `load` | 164 | Load load for the current toolkit workflow. |
| class | `Orchestrator` | 193 | Coordinate orchestrator behavior for the current toolkit workflow. |
| function | `__init__` | 195 | Initialize the instance with validated constructor state. |
| function | `close` | 226 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | 230 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | 234 | Exit the managed runtime context and release owned resources. |
| function | `_transaction` | 238 | Support transaction processing for internal toolkit callers. |
| function | `register` | 242 | Execute the register operation for the current toolkit workflow. |
| function | `_idempotency_key` | 284 | Support idempotency key processing for internal toolkit callers. |
| function | `_event` | 309 | Support event processing for internal toolkit callers. |
| function | `_completed_result_is_intact` | 316 | Verify materialized outputs before reusing a succeeded job. |
| function | `_materialize_outputs` | 341 | Support materialize outputs processing for internal toolkit callers. |
| function | `_dependency_states` | 376 | Support dependency states processing for internal toolkit callers. |
| function | `run` | 387 | Run run for the current toolkit workflow. |
| function | `_set_state` | 420 | Support set state processing for internal toolkit callers. |
| function | `_run_stage` | 436 | Support run stage processing for internal toolkit callers. |
| function | `cancellation_requested` | 515 | Execute the cancellation requested operation for the current toolkit workflow. |
| function | `recover_stale_jobs` | 547 | Reset only RUNNING jobs whose durable heartbeat is older than the bound. |
| function | `cancel` | 592 | Execute the cancel operation for the current toolkit workflow. |
| function | `retry` | 612 | Execute the retry operation for the current toolkit workflow. |
| function | `_update_pipeline_status` | 638 | Support update pipeline status processing for internal toolkit callers. |
| function | `status` | 655 | Execute the status operation for the current toolkit workflow. |
| function | `create_default_pipeline` | 687 | Generate a concrete pipeline for the current project. |

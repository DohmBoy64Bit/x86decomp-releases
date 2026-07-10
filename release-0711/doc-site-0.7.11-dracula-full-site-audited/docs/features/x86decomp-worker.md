---
title: x86decomp.worker
description: Module reference for x86decomp.worker.
---

# `x86decomp.worker`

- Area: `toolkit`
- Source path: `src/x86decomp/worker.py`
- SHA-256: `4ecd317bb9013edb1d0c1b79037ed139d0e240da60703e0b21198b5b131ffe33`
- Size: `14408` bytes
- Lines: `365`

## Module docstring

Bounded command workers with explicit isolation and provenance.

The local worker provides resource and output bounds without pretending to be a
security boundary.  Container mode invokes Docker or Podman with a read-only
root, no network, dropped capabilities, and explicit mounts.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `WorkerLimits` | 27 | Store validated worker limits fields used by toolkit reports and adapters. |
| function | `validate` | 35 | Validate validate for the current toolkit workflow. |
| class | `WorkerRequest` | 43 | Store validated worker request fields used by toolkit reports and adapters. |
| class | `WorkerResult` | 56 | Store validated worker result fields used by toolkit reports and adapters. |
| function | `to_dict` | 73 | Return a serializable dictionary representation. |
| function | `discover_worker_capabilities` | 94 | Discover worker capabilities for the current toolkit workflow. |
| function | `_bounded_environment` | 109 | Support bounded environment processing for internal toolkit callers. |
| function | `_preexec` | 145 | Return the legacy resource-limit callback for API compatibility. |
| function | `apply` | 156 | Execute the apply operation for the current toolkit workflow. |
| function | `_confined_paths` | 172 | Support confined paths processing for internal toolkit callers. |
| function | `_container_command` | 189 | Support container command processing for internal toolkit callers. |
| function | `execute_worker_request` | 215 | Execute the execute worker request operation for the current toolkit workflow. |
| function | `resource_wrapped_command` | 253 | Execute the resource wrapped command operation for the current toolkit workflow. |

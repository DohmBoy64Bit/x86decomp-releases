---
title: x86decomp.service
description: Module reference for x86decomp.service.
---

# `x86decomp.service`

- Area: `toolkit`
- Source path: `src/x86decomp/service.py`
- SHA-256: `07d1d2b97b4b34432e3a60023f1cc5769e62927bb67e118384b361b23fa402e4`
- Size: `9130` bytes
- Lines: `207`

## Module docstring

Optional read-only FastAPI service for project, pipeline, and validation state.

The service never mutates project state.  It exposes durable records produced by
CLI workers and validators so an analyst can inspect a project without granting
the web process write authority.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_json_files` | 24 | Support json files processing for internal toolkit callers. |
| function | `service_snapshot` | 39 | Return a read-only, serializable project-control-plane snapshot. |
| function | `create_app` | 78 | Create app for the current toolkit workflow. |
| function | `health` | 89 | Execute the health operation for the current toolkit workflow. |
| function | `project` | 100 | Execute the project operation for the current toolkit workflow. |
| function | `target_pack` | 105 | Execute the target pack operation for the current toolkit workflow. |
| function | `pipelines` | 117 | Execute the pipelines operation for the current toolkit workflow. |
| function | `convergence` | 122 | Execute the convergence operation for the current toolkit workflow. |
| function | `reproducibility` | 127 | Execute the reproducibility operation for the current toolkit workflow. |
| function | `security` | 132 | Execute the security operation for the current toolkit workflow. |
| function | `functions` | 137 | Execute the functions operation for the current toolkit workflow. |
| function | `workflow` | 151 | Execute the workflow operation for the current toolkit workflow. |
| function | `next_task` | 160 | Execute the next task operation for the current toolkit workflow. |
| function | `reports` | 169 | Execute the reports operation for the current toolkit workflow. |
| function | `index` | 174 | Return the read-only browser UI without injecting project data as HTML. |
| function | `run_service` | 200 | Run service for the current toolkit workflow. |

---
title: x86decomp.project_state
description: Source module reference for x86decomp.project_state.
---

# `x86decomp.project_state`

**Source path:** `src/x86decomp/project_state.py`  
**Documented symbols:** 21

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `ProjectCheck` | class | 70 | 84 | — |
| `to_dict` | function | 77 | 84 | — |
| `ProjectStateDatabase` | class | 87 | 179 | — |
| `__init__` | function | 88 | 103 | — |
| `close` | function | 105 | 106 | — |
| `__enter__` | function | 108 | 109 | — |
| `__exit__` | function | 111 | 112 | — |
| `transaction` | function | 115 | 123 | — |
| `integrity_check` | function | 125 | 127 | — |
| `record_migration` | function | 129 | 147 | — |
| `snapshot` | function | 149 | 168 | — |
| `upsert_artifact_reference` | function | 170 | 176 | — |
| `artifact_digests` | function | 178 | 179 | — |
| `state_database_path` | function | 182 | 183 | — |
| `create_project_backup` | function | 186 | 218 | Create a deterministic gzip tar backup without following symlinks. |
| `_migration_2_to_3` | function | 221 | 249 | — |
| `migrate_project` | function | 252 | 311 | — |
| `check_project_state` | function | 314 | 350 | — |
| `repair_project_state` | function | 353 | 380 | Repair only reconstructible indexes; never rewrite evidence or binaries. |
| `project_gc` | function | 383 | 386 | — |
| `restore_project_backup` | function | 389 | 434 | Safely restore a project backup into an empty destination. |

---
title: x86decomp.project_state
description: Source module reference for x86decomp.project_state.
---

# `x86decomp.project_state`

**Source path:** `src/x86decomp/project_state.py`  
**SHA-256:** `e78c286125050d9b582e38acdefcf3c901f0634372af8b287942ca8b10aa9aee`  
**Documented symbols:** 21

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `ProjectCheck` | class | 70 | 84 | no docstring declared |
| `to_dict` | function | 77 | 84 | no docstring declared |
| `ProjectStateDatabase` | class | 87 | 179 | no docstring declared |
| `__init__` | function | 88 | 103 | no docstring declared |
| `close` | function | 105 | 106 | no docstring declared |
| `__enter__` | function | 108 | 109 | no docstring declared |
| `__exit__` | function | 111 | 112 | no docstring declared |
| `transaction` | function | 115 | 123 | no docstring declared |
| `integrity_check` | function | 125 | 127 | no docstring declared |
| `record_migration` | function | 129 | 147 | no docstring declared |
| `snapshot` | function | 149 | 168 | no docstring declared |
| `upsert_artifact_reference` | function | 170 | 176 | no docstring declared |
| `artifact_digests` | function | 178 | 179 | no docstring declared |
| `state_database_path` | function | 182 | 183 | no docstring declared |
| `create_project_backup` | function | 186 | 218 | Create a deterministic gzip tar backup without following symlinks. |
| `_migration_2_to_3` | function | 221 | 249 | no docstring declared |
| `migrate_project` | function | 252 | 311 | no docstring declared |
| `check_project_state` | function | 314 | 350 | no docstring declared |
| `repair_project_state` | function | 353 | 380 | Repair only reconstructible indexes; never rewrite evidence or binaries. |
| `project_gc` | function | 383 | 386 | no docstring declared |
| `restore_project_backup` | function | 389 | 434 | Safely restore a project backup into an empty destination. |

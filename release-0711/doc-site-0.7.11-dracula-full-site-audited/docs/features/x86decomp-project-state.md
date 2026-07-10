---
title: x86decomp.project_state
description: Module reference for x86decomp.project_state.
---

# `x86decomp.project_state`

- Area: `toolkit`
- Source path: `src/x86decomp/project_state.py`
- SHA-256: `4d988a5e72646f9e1930e2e656398810196323092bc6db62f10ccb81135805ee`
- Size: `20043` bytes
- Lines: `453`

## Module docstring

Transactional project-state database, migrations, backup, and recovery.

This module is intentionally independent from the analysis and work-queue
SQLite databases.  It owns release/schema migration history, durable job state,
artifact references, and project integrity snapshots.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `ProjectCheck` | 70 | Store validated project check fields used by toolkit reports and adapters. |
| function | `to_dict` | 78 | Return a serializable dictionary representation. |
| class | `ProjectStateDatabase` | 89 | Coordinate project state database behavior for the current toolkit workflow. |
| function | `__init__` | 91 | Initialize the instance with validated constructor state. |
| function | `close` | 109 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | 113 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | 117 | Exit the managed runtime context and release owned resources. |
| function | `transaction` | 122 | Execute the transaction operation for the current toolkit workflow. |
| function | `integrity_check` | 133 | Execute the integrity check operation for the current toolkit workflow. |
| function | `record_migration` | 138 | Record migration for the current toolkit workflow. |
| function | `snapshot` | 159 | Execute the snapshot operation for the current toolkit workflow. |
| function | `upsert_artifact_reference` | 181 | Execute the upsert artifact reference operation for the current toolkit workflow. |
| function | `artifact_digests` | 190 | Execute the artifact digests operation for the current toolkit workflow. |
| function | `state_database_path` | 195 | Execute the state database path operation for the current toolkit workflow. |
| function | `create_project_backup` | 200 | Create a deterministic gzip tar backup without following symlinks. |
| function | `_migration_2_to_3` | 235 | Support migration 2 to 3 processing for internal toolkit callers. |
| function | `migrate_project` | 267 | Execute the migrate project operation for the current toolkit workflow. |
| function | `check_project_state` | 330 | Check project state for the current toolkit workflow. |
| function | `repair_project_state` | 370 | Repair only reconstructible indexes; never rewrite evidence or binaries. |
| function | `project_gc` | 400 | Execute the project gc operation for the current toolkit workflow. |
| function | `restore_project_backup` | 407 | Safely restore a project backup into an empty destination. |

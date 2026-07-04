---
title: x86decomp.project_state
description: Transactional project-state database, migrations, backup, and recovery.
---

# `x86decomp.project_state`

Transactional project-state database, migrations, backup, and recovery.

This module is intentionally independent from the analysis and work-queue
SQLite databases.  It owns release/schema migration history, durable job state,
artifact references, and project integrity snapshots.

**Area:** Toolkit  
**Source:** `src/x86decomp/project_state.py`  
**SHA-256:** `2c866a3ccaddff98f1d9342a1eb5397d3dc2bd6d77e4b95c7dd07a8d2e02610f`  
**Functions/methods:** 19

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-projectcheck-to-dict"></a>

### `ProjectCheck.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectCheck.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:ProjectCheck.to_dict`  
**Visibility:** public  
**Source line:** 77

<a id="function-projectstatedatabase-init"></a>

### `ProjectStateDatabase.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.__init__(self, path: Path, *, toolkit_version: str='0.7.5')
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.__init__`  
**Visibility:** internal  
**Source line:** 88

<a id="function-projectstatedatabase-close"></a>

### `ProjectStateDatabase.close`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.close(self) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.close`  
**Visibility:** public  
**Source line:** 105

<a id="function-projectstatedatabase-enter"></a>

### `ProjectStateDatabase.__enter__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.__enter__(self) -> 'ProjectStateDatabase'
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.__enter__`  
**Visibility:** internal  
**Source line:** 108

<a id="function-projectstatedatabase-exit"></a>

### `ProjectStateDatabase.__exit__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.__exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.__exit__`  
**Visibility:** internal  
**Source line:** 111

<a id="function-projectstatedatabase-transaction"></a>

### `ProjectStateDatabase.transaction`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.transaction(self, *, immediate: bool=True) -> Iterator[sqlite3.Connection]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.transaction`  
**Visibility:** public  
**Source line:** 115

<a id="function-projectstatedatabase-integrity-check"></a>

### `ProjectStateDatabase.integrity_check`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.integrity_check(self) -> list[str]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.integrity_check`  
**Visibility:** public  
**Source line:** 125

<a id="function-projectstatedatabase-record-migration"></a>

### `ProjectStateDatabase.record_migration`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.record_migration(self, *, migration_id: str, from_version: int, to_version: int, pre_hash: str, post_hash: str, backup_path: str | None) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.record_migration`  
**Visibility:** public  
**Source line:** 129

<a id="function-projectstatedatabase-snapshot"></a>

### `ProjectStateDatabase.snapshot`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.snapshot(self, project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.snapshot`  
**Visibility:** public  
**Source line:** 149

<a id="function-projectstatedatabase-upsert-artifact-reference"></a>

### `ProjectStateDatabase.upsert_artifact_reference`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.upsert_artifact_reference(self, reference: str, digest: str, kind: str, owner: str) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.upsert_artifact_reference`  
**Visibility:** public  
**Source line:** 170

<a id="function-projectstatedatabase-artifact-digests"></a>

### `ProjectStateDatabase.artifact_digests`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectStateDatabase.artifact_digests(self) -> set[str]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.artifact_digests`  
**Visibility:** public  
**Source line:** 178

<a id="function-state-database-path"></a>

### `state_database_path`

No function or method docstring is declared in the 0.7.5 source.

```python
def state_database_path(project_root: Path) -> Path
```

**Catalog symbol:** `x86decomp.project_state:state_database_path`  
**Visibility:** public  
**Source line:** 182

<a id="function-create-project-backup"></a>

### `create_project_backup`

Create a deterministic gzip tar backup without following symlinks.

```python
def create_project_backup(project_root: Path, output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:create_project_backup`  
**Visibility:** public  
**Source line:** 186

<a id="function-migration-2-to-3"></a>

### `_migration_2_to_3`

No function or method docstring is declared in the 0.7.5 source.

```python
def _migration_2_to_3(root: Path, project: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:_migration_2_to_3`  
**Visibility:** internal  
**Source line:** 221

<a id="function-migrate-project"></a>

### `migrate_project`

No function or method docstring is declared in the 0.7.5 source.

```python
def migrate_project(project_root: Path, *, dry_run: bool=False, backup_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:migrate_project`  
**Visibility:** public  
**Source line:** 252

<a id="function-check-project-state"></a>

### `check_project_state`

No function or method docstring is declared in the 0.7.5 source.

```python
def check_project_state(project_root: Path) -> ProjectCheck
```

**Catalog symbol:** `x86decomp.project_state:check_project_state`  
**Visibility:** public  
**Source line:** 314

<a id="function-repair-project-state"></a>

### `repair_project_state`

Repair only reconstructible indexes; never rewrite evidence or binaries.

```python
def repair_project_state(project_root: Path, *, dry_run: bool=True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:repair_project_state`  
**Visibility:** public  
**Source line:** 353

<a id="function-project-gc"></a>

### `project_gc`

No function or method docstring is declared in the 0.7.5 source.

```python
def project_gc(project_root: Path, *, dry_run: bool=True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:project_gc`  
**Visibility:** public  
**Source line:** 383

<a id="function-restore-project-backup"></a>

### `restore_project_backup`

Safely restore a project backup into an empty destination.

```python
def restore_project_backup(archive_path: Path, destination: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:restore_project_backup`  
**Visibility:** public  
**Source line:** 389

---
title: x86decomp.project_state
description: Transactional project-state database, migrations, backup, and recovery.
original_path: features/x86decomp-project-state.html
---

<a id="function-projectcheck-to-dict"></a>
<a id="function-projectstatedatabase-init"></a>
<a id="function-projectstatedatabase-close"></a>
<a id="function-projectstatedatabase-enter"></a>
<a id="function-projectstatedatabase-exit"></a>
<a id="function-projectstatedatabase-transaction"></a>
<a id="function-projectstatedatabase-integrity-check"></a>
<a id="function-projectstatedatabase-record-migration"></a>
<a id="function-projectstatedatabase-snapshot"></a>
<a id="function-projectstatedatabase-upsert-artifact-reference"></a>
<a id="function-projectstatedatabase-artifact-digests"></a>
<a id="function-state-database-path"></a>
<a id="function-create-project-backup"></a>
<a id="function-migration-2-to-3"></a>
<a id="function-migrate-project"></a>
<a id="function-check-project-state"></a>
<a id="function-repair-project-state"></a>
<a id="function-project-gc"></a>
<a id="function-restore-project-backup"></a>

Section: Source-derived feature and function reference

# x86decomp.project_state

Transactional project-state database, migrations, backup, and recovery.

Metadata: core · current · 19 functions/methods

**Source:** `src/x86decomp/project_state.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `8d063061a36ef9a66f1460e44c8a5f2e08bd239e8c3c6d9828f4bfc171bb1fbe`.

## Functions and methods

Metadata: public · line 77

### ProjectCheck.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:ProjectCheck.to_dict`

Metadata: internal · line 88

### ProjectStateDatabase.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, path: Path, *, toolkit_version: str = '0.7.4')
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.__init__`

Metadata: public · line 105

### ProjectStateDatabase.close

No function or method docstring is declared in the v0.7.4 source.

```
def close(self) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.close`

Metadata: internal · line 108

### ProjectStateDatabase.__enter__

No function or method docstring is declared in the v0.7.4 source.

```
def __enter__(self) -> 'ProjectStateDatabase'
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.__enter__`

Metadata: internal · line 111

### ProjectStateDatabase.__exit__

No function or method docstring is declared in the v0.7.4 source.

```
def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.__exit__`

Metadata: public · line 115

### ProjectStateDatabase.transaction

No function or method docstring is declared in the v0.7.4 source.

```
def transaction(self, *, immediate: bool = True) -> Iterator[sqlite3.Connection]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.transaction`

Metadata: public · line 125

### ProjectStateDatabase.integrity_check

No function or method docstring is declared in the v0.7.4 source.

```
def integrity_check(self) -> list[str]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.integrity_check`

Metadata: public · line 129

### ProjectStateDatabase.record_migration

No function or method docstring is declared in the v0.7.4 source.

```
def record_migration(self, *, migration_id: str, from_version: int, to_version: int, pre_hash: str, post_hash: str, backup_path: str | None) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.record_migration`

Metadata: public · line 149

### ProjectStateDatabase.snapshot

No function or method docstring is declared in the v0.7.4 source.

```
def snapshot(self, project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.snapshot`

Metadata: public · line 170

### ProjectStateDatabase.upsert_artifact_reference

No function or method docstring is declared in the v0.7.4 source.

```
def upsert_artifact_reference(self, reference: str, digest: str, kind: str, owner: str) -> None
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.upsert_artifact_reference`

Metadata: public · line 178

### ProjectStateDatabase.artifact_digests

No function or method docstring is declared in the v0.7.4 source.

```
def artifact_digests(self) -> set[str]
```

**Catalog symbol:** `x86decomp.project_state:ProjectStateDatabase.artifact_digests`

Metadata: public · line 182

### state_database_path

No function or method docstring is declared in the v0.7.4 source.

```
def state_database_path(project_root: Path) -> Path
```

**Catalog symbol:** `x86decomp.project_state:state_database_path`

Metadata: public · line 186

### create_project_backup

Create a deterministic gzip tar backup without following symlinks.

```
def create_project_backup(project_root: Path, output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:create_project_backup`

Metadata: internal · line 221

### _migration_2_to_3

No function or method docstring is declared in the v0.7.4 source.

```
def _migration_2_to_3(root: Path, project: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:_migration_2_to_3`

Metadata: public · line 252

### migrate_project

No function or method docstring is declared in the v0.7.4 source.

```
def migrate_project(project_root: Path, *, dry_run: bool = False, backup_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:migrate_project`

Metadata: public · line 314

### check_project_state

No function or method docstring is declared in the v0.7.4 source.

```
def check_project_state(project_root: Path) -> ProjectCheck
```

**Catalog symbol:** `x86decomp.project_state:check_project_state`

Metadata: public · line 353

### repair_project_state

Repair only reconstructible indexes; never rewrite evidence or binaries.

```
def repair_project_state(project_root: Path, *, dry_run: bool = True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:repair_project_state`

Metadata: public · line 383

### project_gc

No function or method docstring is declared in the v0.7.4 source.

```
def project_gc(project_root: Path, *, dry_run: bool = True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:project_gc`

Metadata: public · line 389

### restore_project_backup

Safely restore a project backup into an empty destination.

```
def restore_project_backup(archive_path: Path, destination: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.project_state:restore_project_backup`

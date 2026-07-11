# Project: Operations and Recovery

## `x86decomp project-check`

Validates a project's on-disk state and collects integrity failures and warnings.

### Synopsis

```bash
x86decomp project-check PROJECT
```

### Purpose

Reads `project.json`, checks schema version (must be 3), binary presence and hash, project-state database integrity and schema version, and content store integrity. This is a compatibility alias that delegates to `x86decomp project check` internally via `_compatibility_alias`.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | Yes | path | Project root directory containing `project.json`. |

### Return value

A `ProjectCheck` object serialized to JSON:

| Field | Description |
|---|---|
| `valid` | `true` when zero failures. |
| `failures` | List of failure strings (empty when healthy). |
| `warnings` | List of advisory warnings. |
| `project_schema_version` | Observed schema version from `project.json`. |
| `state_db_schema_version` | Observed schema version from `state/project-state.sqlite3`. |

### Checks performed

1. `project.json` exists and is a valid object.
2. Schema version is 3 (older versions produce a failure recommending migration).
3. Binary file exists at the resolved path.
4. Binary SHA-256 matches the recorded hash.
5. Project-state database (`state/project-state.sqlite3`) exists.
6. Project-state database passes `PRAGMA integrity_check`.
7. State database schema version is read and recorded.
8. Content store directory exists.
9. Content store passes its internal integrity verification.

### Example

```bash
x86decomp project-check ./myproject
```

```json
{
  "valid": true,
  "failures": [],
  "warnings": [],
  "project_schema_version": 3,
  "state_db_schema_version": 1
}
```

### Related commands

- [`verify-project`](init-verify.md#x86decomp-verify-project) — broader verification covering schema v1–v3
- [`project-migrate`](#x86decomp-project-migrate) — migrate to schema v3
- [`project-repair`](#x86decomp-project-repair) — repair reconstructible indexes

---

## `x86decomp project-migrate`

Migrates `project.json` forward to schema version 3, with backup and audit trail.

### Synopsis

```bash
x86decomp project-migrate PROJECT [--dry-run] [--backup BACKUP]
```

### Purpose

Supports migration from schema 1 or 2 to schema 3. Schema v3 adds the project-state database, content store, target-pack path, and orchestration root. Unless `--dry-run` is set, a pre-migration backup is created, the project file is rewritten, and the migration is recorded with a snapshot in the project-state database.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | Yes | path | Project root containing `project.json`. |

### Options

| Option | Default | Description |
|---|---|---|
| `--dry-run` | off | Compute and return the migration plan without modifying anything. Returns `project_preview` showing the projected post-migration state. |
| `--backup` | `{PROJECT}-pre-migration-backup.tar.gz` (sibling of project root) | Explicit backup destination path. |

### Migration paths

| From | To | Changes |
|---|---|---|
| 1 | 2 | Adds `schema_version: 2`, `default_modes`, `analysis_database` path, `work_queue` path. |
| 2 | 3 | Creates `state/`, `artifacts/`, `orchestration/` dirs, `target-pack/`, report dirs, `templates/`. Initializes project-state database (schema v1) and content store. |
| 3 | 3 | No-op. Returns `{changed: false, ...}`. |

### Return value (applied)

```json
{
  "changed": true,
  "from_version": 2,
  "to_version": 3,
  "dry_run": false,
  "plan": ["2->3"],
  "backup": {"path": "/path/to/backup.tar.gz", "sha256": "...", "file_count": 42, "size": 512000},
  "snapshot": {"snapshot_id": "...", "project_json_sha256": "...", "state": {...}}
}
```

### Example

```bash
# Preview the plan
x86decomp project-migrate ./myproject --dry-run

# Apply with default backup location
x86decomp project-migrate ./myproject

# Apply with explicit backup
x86decomp project-migrate ./myproject --backup /safe/backups/myproject-pre.tar.gz
```

### Related commands

- [`project-check`](#x86decomp-project-check) — check current state before migration
- [`project-backup`](#x86decomp-project-backup) — manual backup

---

## `x86decomp project-backup`

Creates a deterministic gzip tar backup of the entire project tree.

### Synopsis

```bash
x86decomp project-backup PROJECT OUTPUT
```

### Purpose

Recursively walks the project root, collects all regular files (sorted by path for determinism), and writes a gzip-compressed PAX-format tar archive with normalized metadata: `uid=0`, `gid=0`, `uname=""`, `gname=""`, `mtime=0`, `mode=0o644`, `mtime=0` on the gzip stream.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | Yes | path | Project root containing `project.json`. |
| `OUTPUT` | Yes | path | Output archive path. Must be **outside** the project tree. |

### Safety constraints

- Rejects symlinks anywhere in the project tree.
- Rejects output paths inside the project tree.
- Writes to a temporary file first, then atomically renames to `OUTPUT`.

### Example

```bash
x86decomp project-backup ./myproject ./backups/myproject-2025-07-11.tar.gz
```

```json
{
  "path": "/abs/path/to/backups/myproject-2025-07-11.tar.gz",
  "sha256": "abc123...",
  "file_count": 147,
  "size": 1048576
}
```

### Related commands

- [`project-restore`](#x86decomp-project-restore) — restore from backup
- [`project-migrate`](#x86decomp-project-migrate) — creates a backup before migration

---

## `x86decomp project-restore`

Safely restores a project backup into an empty destination.

### Synopsis

```bash
x86decomp project-restore ARCHIVE DESTINATION
```

### Purpose

Extracts a previously backed-up project from a gzip tar archive. Applies safety checks before extraction: rejects absolute paths, `..` traversal, symlinks, hard links, device nodes, files over 2 GiB, total expansion over 8 GiB, more than 100,000 members, missing `project.json`, and non-empty destinations. Extracts through a staging directory, then moves contents to the destination atomically. Runs `project-check` on the restored project.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `ARCHIVE` | Yes | path | Gzip tar archive from `project-backup`. Must be a regular file. |
| `DESTINATION` | Yes | path | Empty directory to receive the restored project. |

### Safety constraints

| Check | Limit |
|---|---|
| Archive member count | ≤ 100,000 |
| Single root directory | Exactly one top-level dir |
| No absolute paths or `..` | Rejected |
| No symlinks, hard links, devices | Rejected |
| Per-member size | ≤ 2 GiB |
| Total expansion | ≤ 8 GiB |
| Destination must be empty | Required |
| Archive must contain `project.json` | Required |

### Example

```bash
x86decomp project-restore ./backups/myproject-2025-07-11.tar.gz ./restored-project
```

```json
{
  "restored": true,
  "destination": "/abs/path/to/restored-project",
  "archive_sha256": "abc123...",
  "check": {
    "valid": true,
    "failures": [],
    "warnings": [],
    "project_schema_version": 3,
    "state_db_schema_version": 1
  }
}
```

### Related commands

- [`project-backup`](#x86decomp-project-backup) — create the backup
- [`project-check`](#x86decomp-project-check) — manual integrity check

---

## `x86decomp project-repair`

Inspects or applies deterministic repairs to reconstructible project indexes.

### Synopsis

```bash
x86decomp project-repair PROJECT [--apply]
```

### Purpose

Repairs only reconstructible indexes and missing empty infrastructure that can be derived safely. Never rewrites target bytes, evidence, claims, or candidate source. Repairs performed:

1. Creates the project-state database if missing.
2. Creates the content store directory if missing.
3. Restores missing content-store artifact references from the state database.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | Yes | path | Project root containing `project.json`. |

### Options

| Option | Default | Description |
|---|---|---|
| `--apply` | off (dry-run) | When set, applies repairs. Without it, only reports what would be done. |

### Example

```bash
# Inspect what needs repair
x86decomp project-repair ./myproject

# Apply repairs
x86decomp project-repair ./myproject --apply
```

```json
{
  "dry_run": true,
  "actions": [
    {"action": "create_content_store", "path": "/path/to/myproject/artifacts"}
  ],
  "changed": false
}
```

### Related commands

- [`project-check`](#x86decomp-project-check) — identify issues first
- [`project-gc`](#x86decomp-project-gc) — garbage-collect content store

---

## `x86decomp project-gc`

Garbage-collects unreferenced objects from the project content store.

### Synopsis

```bash
x86decomp project-gc PROJECT [--apply]
```

### Purpose

Deletes only content-store objects that are not referenced by any active artifact reference. Defaults to dry-run mode for safety.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | Yes | path | Project root containing `project.json`. |

### Options

| Option | Default | Description |
|---|---|---|
| `--apply` | off (dry-run) | When set, actually deletes unreferenced objects. Without it, only reports reclaimable space. |

### Example

```bash
# Preview reclaimable objects
x86decomp project-gc ./myproject

# Actually delete them
x86decomp project-gc ./myproject --apply
```

### Related commands

- [`project-repair`](#x86decomp-project-repair) — repair before collecting
- [`content-verify`](../content-store.md) — verify content store integrity

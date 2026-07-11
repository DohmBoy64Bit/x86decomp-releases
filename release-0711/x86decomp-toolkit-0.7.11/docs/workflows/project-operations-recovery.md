# Project Operations and Recovery

**Technical objective:** Full project lifecycle management — initialization, checkpointing, schema migration, backup/restore, corruption simulation and repair, garbage collection, and integrity verification — with project memory as the audit ledger.

**Game:** Shadow Circuit (fictional stealth action game, x86 PE32, ~2.3 MB executable).

---

## Overview

Shadow Circuit is in active matching decompilation with 12 contributors across three time zones. The project has accumulated 1,800+ function workflow states, 340 evidence records, 72 claims, three compiler profiles, and a 4 GB content-addressed artifact store. A team lead needs to run scheduled maintenance, simulate a catastrophic state corruption, and demonstrate full recovery without data loss.

You will learn:

1. How to initialize a project and take regular project-state checkpoints.
2. How to migrate project schemas across toolkit versions.
3. How to back up, simulate corruption, repair, and restore project state.
4. How to garbage-collect unreferenced artifacts.
5. How to verify project integrity and audit the memory ledger.

---

## Prerequisites

| Requirement | Detail |
|---|---|
| **Binary** | `games/shadow-circuit/shadow_circuit.exe` — PE32 x86 |
| **Project** | `games/shadow-circuit/project/` (approx. 5 GB) |
| **Disk space** | At least 2x project size for backup staging |
| **Permissions** | Read/write on project directory and backup destination |

---

## Starting directory structure

```
games/shadow-circuit/
├── shadow_circuit.exe
└── project/
    ├── project.json
    ├── original/
    ├── functions/
    ├── artifacts/
    ├── build/
    ├── evidence/
    ├── memory/                    # project memory ledger
    │   └── events.jsonl
    ├── state/
    │   └── project-state.sqlite3
    ├── analysis/
    │   └── database/
    │       └── analysis.sqlite3
    ├── orchestration/
    └── reports/
```

---

## Step 1: Initialize and take the first checkpoint

```console
$ x86decomp init games/shadow-circuit/shadow_circuit.exe games/shadow-circuit/project/
$ x86decomp project-check games/shadow-circuit/project/
$ x86decomp snapshot-tools --output games/shadow-circuit/project/config/tools.json
```

**What happens:** `init` creates the full project tree. `project-check` validates the project state database, binary hash, and directory structure immediately after initialization. `snapshot-tools` records the current tool environment.

Add a project-memory entry to mark the initialization:
```console
$ x86decomp memory-add games/shadow-circuit/project/ \
    --actor lead-analyst \
    --category milestone \
    --summary "Project initialized for Shadow Circuit v1.0 release binary" \
    --details-json '{"binary_sha256": "abc...", "team_size": 12}'

$ x86decomp memory-verify games/shadow-circuit/project/
```

**What happens:** `memory-add` appends an evidence-linked entry to `memory/events.jsonl`. `memory-verify` checks the integrity of all memory entries — verifying each entry's cryptographic chain and cross-referenced evidence IDs still exist.

!!! note "Project memory is append-only"
    Project memory entries are never modified or deleted. They form an immutable audit ledger. Use `memory-render` to export the full ledger as Markdown for human review.

---

## Step 2: Simulate regular checkpointing with project-check

After significant work (new evidence, matched functions, compiler profile changes), validate state:

```console
$ x86decomp project-check games/shadow-circuit/project/
```

Add a checkpoint memory entry:
```console
$ x86decomp memory-add games/shadow-circuit/project/ \
    --actor lead-analyst \
    --category checkpoint \
    --summary "Weekly checkpoint: 340 functions matched, 72 claims verified" \
    --details-json '{"matched_functions": 340, "verified_claims": 72, "toolkit_release": "0.7.11"}'
```

**Expected output from `project-check`:**
```json
{
  "project_id": "x86d-...",
  "valid": true,
  "failures": [],
  "schema_version": 3,
  "checks_passed": 14,
  "memory_event_count": 2
}
```

---

## Step 3: Migrate the project schema

When upgrading the toolkit, project state may need migrating:

```console
$ x86decomp project-migrate games/shadow-circuit/project/ --dry-run
```

**What happens:** Dry-run mode reports which schema transformations would be applied without modifying anything. Review the output to confirm the migration plan is safe.

```console
$ x86decomp project-migrate games/shadow-circuit/project/ \
    --backup games/shadow-circuit/backups/pre-migrate-2026-07-11.tar.gz
```

**What happens:** `project-migrate` with `--backup` creates a deterministic gzip/tar backup before applying the migration, then writes migration provenance to the state database. If the migration fails partway through, the project is still recoverable from the backup.

!!! warning "Migration is monotonic"
    Schema migrations are forward-only. Once migrated, the project cannot be downgraded. Always take a backup before migrating.

---

## Step 4: Create a deterministic backup

```console
$ x86decomp project-backup games/shadow-circuit/project/ \
    games/shadow-circuit/backups/shadow-circuit-2026-07-11.tar.gz
```

**What happens:** `project-backup` creates a deterministic gzip/tar archive with:
- Normalized file timestamps (epoch 0)
- Sorted archive entry order
- Exclusion of system files and temporary artifacts
- SHA-256 manifest embedded in the archive header
- Rejection of symlinks (backups are filesystem-portable)

Verify the backup with content-addressed storage:
```console
$ x86decomp content-put games/shadow-circuit/project/artifacts/ \
    games/shadow-circuit/backups/shadow-circuit-2026-07-11.tar.gz \
    --reference backup-2026-07-11 --kind backup
$ x86decomp content-verify games/shadow-circuit/project/artifacts/
```

**What happens:** `content-put` stores the backup by its cryptographic digest in the content-addressed artifact store. `content-verify` confirms all stored objects have correct digests.

---

## Step 5: Simulate corruption and inspect

To demonstrate recovery, simulate a corrupted state database (on a disposable copy):

```console
# WARNING: For demonstration only — corrupt a copy, never the live project
```

Run a dry-run repair to see what would be detected and fixed:

```console
$ x86decomp project-repair games/shadow-circuit/project/
```

**What happens:** `project-repair` (without `--apply`) inspects the project for:
- Missing or corrupt state database indexes
- Orphaned content-store references
- Broken evidence-to-file chains
- Missing empty infrastructure directories
- Stale orchestration job records

Example dry-run output:
```json
{
  "dry_run": true,
  "issues_found": 3,
  "issues": [
    {"kind": "missing_index", "detail": "state/idx_workflow_function_id missing"},
    {"kind": "orphaned_reference", "detail": "content-store digest a1b2c3... unreferenced"},
    {"kind": "missing_directory", "detail": "orchestration/logs/ empty, will recreate"}
  ],
  "repairs_available": 3
}
```

---

## Step 6: Apply repairs

```console
$ x86decomp project-repair games/shadow-circuit/project/ --apply
```

**What happens:** `project-repair --apply` reconstructs missing indexes, removes unreferenced orphan references from the content-store index, and recreates empty required directories. It **does not** rewrite target bytes, evidence records, claims, or candidate source code.

!!! danger "Repair boundaries"
    Project repair only reconstructs *derivable* infrastructure — indexes, caches, directories. It never modifies the original binary, evidence, claims, function workflows, or candidate source. If evidence files are corrupted, repair reports them as irreparable.

---

## Step 7: Restore from backup (full recovery)

If repair cannot fix the issue, restore from the last good backup:

```console
$ x86decomp project-restore games/shadow-circuit/backups/shadow-circuit-2026-07-11.tar.gz \
    games/shadow-circuit/project-restored/
```

**What happens:** `project-restore` validates the archive, rejects path traversal and absolute paths, then extracts through a staging directory into the destination. After extraction, it:
- Verifies the `project.json` schema version matches the backup
- Validates the binary SHA-256 against the stored hash
- Runs `verify-project` internally and reports results

Confirm the restored project:
```console
$ x86decomp verify-project games/shadow-circuit/project-restored/
```

**Expected output:**
```json
{
  "project_id": "x86d-...",
  "valid": true,
  "failures": [],
  "restored_from": "shadow-circuit-2026-07-11.tar.gz"
}
```

Cross-reference project memory before and after:
```console
$ x86decomp memory-render games/shadow-circuit/project/
$ x86decomp memory-render games/shadow-circuit/project-restored/
```

**What happens:** `memory-render` exports the full project memory ledger as Markdown. Compare the two outputs — they should be identical if the backup was taken before any corruption.

---

## Step 8: Garbage-collect unreferenced content

Over months of active decompilation, content-addressed artifacts accumulate unreferenced blobs:

```console
$ x86decomp project-gc games/shadow-circuit/project/
```

**What happens (dry-run):** `project-gc` scans the content-store index, cross-references every digest against active workflow candidates, evidence files, and pipeline outputs, and reports unreferenced objects and their total size.

```json
{
  "dry_run": true,
  "unreferenced_objects": 147,
  "total_bytes_recoverable": 214302720,
  "objects": [
    {"digest": "sha256:abc...", "size": 1536, "age_days": 34}
  ]
}
```

Apply gc:
```console
$ x86decomp project-gc games/shadow-circuit/project/ --apply
```

**What happens:** `project-gc --apply` deletes only the unreferenced content-store objects. It does not touch `functions/`, `evidence/`, `src/`, or any other directory. GC is safe — the toolkit never deletes anything in a referenced state.

---

## Step 9: Final integrity verification

```console
$ x86decomp verify-project games/shadow-circuit/project/
$ x86decomp memory-verify games/shadow-circuit/project/
$ x86decomp memory-render games/shadow-circuit/project/ > project-audit.md
```

**Confirmation checklist:**
- `verify-project` returns `valid: true` with zero failures
- `memory-verify` returns `valid: true` — every memory entry has intact cryptographic chain
- Project memory ledger shows a clear audit trail: init → checkpoints → backup → repair → restore → gc
- Content store passes `content-verify`

---

## Expected state after each stage

| Stage | Key state change |
|---|---|
| **init + project-check** | `project.json` version 3, state database initialized, 1 memory event |
| **project-migrate** | State schema version bumped, backup created, migration provenance recorded |
| **project-backup** | Deterministic `.tar.gz` at backup path, content-store entry |
| **project-repair (dry)** | Report of issues without modifications |
| **project-repair (apply)** | Indexes reconstructed, orphans cleaned, directories created |
| **project-restore** | Full project tree at destination, `verify-project` passes |
| **project-gc** | Unreferenced content-store objects deleted |

---

## Common failure cases and recovery

| Failure | Cause | Recovery |
|---|---|---|
| `project-backup` fails on symlink | Project tree contains a symlink | Remove symlinks; backups are filesystem-portable |
| `project-restore` rejects archive | Path traversal or absolute path detected | Re-create backup from a clean project tree |
| `project-migrate` fails mid-migration | Disk full or power loss during schema transformation | Restore from pre-migration backup, retry |
| `project-repair` reports irreparable evidence | Evidence file missing or corrupted | Restore from backup; repairs cannot recreate evidence |
| `project-gc` dry-run shows unexpected objects | Orphaned pipeline outputs or stale cache entries | Review objects list; only proceed if identified as safe |
| `memory-verify` fails | Broken cryptographic chain in `events.jsonl` | Inspect the specific event entry; manual correction may be needed |

---

## Related reference pages

- [Project Operations](../commands/project/operations.md)
- [init / verify-project](../commands/project/init-verify.md)
- [Project Memory](../commands/workflow/memory.md)
- [Pipeline Commands](../commands/pipeline/pipeline.md)
- [Project Schema](../config/project.md)
- [Content Store](../commands/content-store.md)
- [Operations and Recovery](../operations-and-recovery.md)

---

## Optional extensions

1. **Scheduled maintenance pipeline:** Create a `pipeline-create` manifest that chains `project-check`, `project-backup`, `project-gc --apply`, and `memory-render` into a single automated workflow. Run weekly via `pipeline-run`.

2. **Multi-project snapshot comparison:** Use `snapshot-tools` across multiple projects and compare tool version differences with `diff-bytes` on the snapshot files to detect drift.

3. **Remote backup via content store:** After `content-put` of the backup, use the content-addressed digest to verify the backup at a remote location without re-transferring:
   ```console
   $ x86decomp content-verify games/shadow-circuit/project/artifacts/
   ```

4. **Automated repair before pipeline runs:** Add a `project-repair` step as the first stage of every pipeline manifest to ensure a clean state before long-running operations.

5. **Evidence migration tracking:** After `project-migrate`, run `evidence-add` to record the migration as an observed event with `--kind observed --source project-migrate`. This creates an audit chain from schema v2 to v3.

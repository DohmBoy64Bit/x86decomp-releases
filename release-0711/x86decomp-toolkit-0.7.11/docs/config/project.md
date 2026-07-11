# Project configuration

`$id: urn:x86decomp:schema:project:3` — schema versions 1, 2, and 3.

Validated against `schemas/project.schema.json`.

---

## Top-level fields

| Field | Type | Required | Default |
|-------|------|----------|---------|
| `schema_version` | `1 \| 2 \| 3` | yes | — |
| `project_id` | string (pattern) | yes | — |
| `created_at` | string (date-time) | yes | — |
| `supported_scope` | enum | yes | — |
| `binary` | object | yes | — |
| `program_manifest` | string | yes | — |
| `memory_ledger` | string | yes | — |
| `function_root` | string | yes | — |
| `evidence_root` | string | yes | — |
| `status` | enum | yes | — |

### `schema_version`

Determines which additional fields are required:

- **1** — original schema: x86-only, no `architecture`, `analysis_database`, or `work_queue`.
- **2** — adds `architecture`, `default_modes`, `analysis_database`, `work_queue` as required.
- **3** — adds `project_state_database`, `content_store`, `target_pack`, `orchestration_root`, `toolkit_release` as required.

### `project_id`

Pattern: `^(?:x86d\|x64d)-[0-9a-f]{16}-[0-9a-f]{8}$`

The prefix is `x86d` for x86 binaries, `x64d` for x86_64 binaries. Generated from the first 16 hex digits of the binary SHA-256 plus 8 random hex digits.

```text
x86d-0123456789abcdef-deadbeef
x64d-fedcba9876543210-1a2b3c4d
```

### `supported_scope`

| Value | Meaning |
|-------|---------|
| `native Windows PE32 x86` | 32-bit x86 Windows PE (v1 only, or x86 projects) |
| `native Windows PE32+ x86-64` | 64-bit x86-64 Windows PE (v2/v3 only) |

### `status`

| Value | Meaning |
|-------|---------|
| `initialized` | Project created, no work done |
| `analyzing` | Static analysis in progress |
| `active` | Decompilation work underway |
| `archived` | Project completed or shelved |

---

## `binary` object

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `name` | string | yes | minLength 1 |
| `source_kind` | enum | yes | `copied` or `external_reference` |
| `path` | string | yes | minLength 1 |
| `sha256` | string | yes | 64 lowercase hex chars |
| `size` | integer | yes | minimum 1 |

`source_kind` records whether the binary was copied into the project (`copied`) or references an external path (`external_reference`).

!!! note
    When `copy_binary=False` during init, `source_kind` is `external_reference` and `path` is an absolute path outside the project root.

---

## Version-conditional fields

### All versions

| Field | Type | Meaning |
|-------|------|---------|
| `program_manifest` | string | Path to the PE program manifest JSON (default: `analysis/program.json`) |
| `memory_ledger` | string | Path to the memory event ledger (default: `memory/events.jsonl`) |
| `function_root` | string | Root directory for function packets (default: `functions`) |
| `evidence_root` | string | Root directory for evidence store (default: `evidence`) |

### V2+ (schema_version 2 or 3)

| Field | Type | Meaning |
|-------|------|---------|
| `architecture` | `x86 \| x86_64` | Target architecture |
| `default_modes` | const `["matching", "functional"]` | Decompilation modes enabled |
| `analysis_database` | string | Path to SQLite analysis database (default: `analysis/database/analysis.sqlite3`) |
| `work_queue` | string | Path to SQLite work queue (default: `work/tasks.sqlite3`) |

### V3 only (schema_version 3)

| Field | Type | Meaning |
|-------|------|---------|
| `project_state_database` | string | Path to SQLite project state DB (default: `state/project-state.sqlite3`) |
| `content_store` | string | Path to content-addressed artifact store (default: `artifacts`) |
| `target_pack` | string | Path to target pack TOML (default: `target-pack/target.toml`) |
| `target_id` | string (optional) | Canonical target identifier |
| `template_kind` | `matching \| functional \| hybrid` (optional) | Project template classification |
| `orchestration_root` | string | Root for orchestration artifacts (default: `orchestration`) |
| `toolkit_release` | string (pattern `^\d+\.\d+\.\d+$`) | Toolkit version that initialized the project |

---

## Example (v3)

```json
{
  "schema_version": 3,
  "project_id": "x86d-0123456789abcdef-deadbeef",
  "created_at": "2026-07-01T12:00:00Z",
  "supported_scope": "native Windows PE32 x86",
  "architecture": "x86",
  "default_modes": ["matching", "functional"],
  "binary": {
    "name": "target.exe",
    "source_kind": "copied",
    "path": "original/target.exe",
    "sha256": "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789",
    "size": 102400
  },
  "program_manifest": "analysis/program.json",
  "analysis_database": "analysis/database/analysis.sqlite3",
  "work_queue": "work/tasks.sqlite3",
  "memory_ledger": "memory/events.jsonl",
  "function_root": "functions",
  "evidence_root": "evidence",
  "project_state_database": "state/project-state.sqlite3",
  "content_store": "artifacts",
  "target_pack": "target-pack/target.toml",
  "orchestration_root": "orchestration",
  "toolkit_release": "0.7.11",
  "status": "active"
}
```

!!! tip
    The project file is written to `project.json` in the project root and validated by `x86decomp project verify`.

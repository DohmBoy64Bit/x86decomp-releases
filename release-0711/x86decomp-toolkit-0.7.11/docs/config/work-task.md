# Work task

`$id: urn:x86decomp:schema:work-task:1` — schema version 1.

Validated against `schemas/work-task.schema.json`.

A work task is a validator-gated work item that tracks the decompilation lifecycle of a single function from queuing through proposal, validation, and acceptance or rejection.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `id` | string | Pattern `^task-[0-9a-f]{32}$` |
| `function_id` | string | Pattern `^pe-rva:[0-9a-f]{8}$` |
| `mode` | enum | `matching` or `functional` |
| `kind` | string | Task category (free-form) |
| `status` | enum | One of 7 values |
| `priority` | integer | — |
| `instructions` | string | minLength 1 |
| `required_validators` | array of strings | minItems 1, uniqueItems |
| `validator_results` | object (string→object) | Per-validator results |
| `evidence_ids` | array of strings | — |
| `created_at` | string | date-time format |
| `updated_at` | string | date-time format |

---

### `id` pattern

Must match `^task-[0-9a-f]{32}$`. Example: `task-a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`

### `function_id` pattern

Must match `^pe-rva:[0-9a-f]{8}$`. Example: `pe-rva:00001000`

### `status` values (7 total)

| Value | Meaning |
|-------|---------|
| `queued` | Task is in the queue, not yet assigned |
| `claimed` | An assignee has claimed the task |
| `proposed` | A proposal (source code) has been submitted |
| `validating` | Automated validators are running |
| `accepted` | All validators passed |
| `rejected` | One or more validators failed |
| `blocked` | Progress is blocked (dependency, missing info) |

---

## Optional fields

| Field | Type | Default | Meaning |
|-------|------|---------|---------|
| `assignee` | string or null | — | Who is working on this task |
| `proposal` | object or null | — | The submitted decompilation proposal |

---

## Validator results

Each key in `validator_results` is a validator name. Each value is an object:

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `report_path` | string | yes | Path to the validator report |
| `passed` | boolean | yes | Whether validation passed |
| `recorded_at` | string | yes | date-time format |

---

## Example

```json
{
  "id": "task-a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
  "function_id": "pe-rva:00001000",
  "mode": "matching",
  "kind": "pe_function",
  "status": "accepted",
  "priority": 1,
  "instructions": "Decompile function at 0x1000 for byte-identical matching under msvc6 /O2.",
  "assignee": "analyst-jd",
  "proposal": {
    "source_file": "src/matched/s_game_init.c",
    "sha256": "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789"
  },
  "required_validators": ["compiles", "byte_match", "abi_compat"],
  "validator_results": {
    "compiles": {
      "report_path": "reports/matching/task-a1b2c3d4/compile.json",
      "passed": true,
      "recorded_at": "2026-07-01T12:00:00Z"
    },
    "byte_match": {
      "report_path": "reports/matching/task-a1b2c3d4/byte-compare.json",
      "passed": true,
      "recorded_at": "2026-07-01T12:01:00Z"
    },
    "abi_compat": {
      "report_path": "reports/matching/task-a1b2c3d4/abi.json",
      "passed": true,
      "recorded_at": "2026-07-01T12:02:00Z"
    }
  },
  "evidence_ids": [
    "ev.static-analysis.1000",
    "ev.compiler-output.1000"
  ],
  "created_at": "2026-07-01T10:00:00Z",
  "updated_at": "2026-07-01T12:02:00Z"
}
```

!!! tip
    The `required_validators` list defines which gates must pass. Each validator in the list should have a corresponding key in `validator_results` once validation runs.

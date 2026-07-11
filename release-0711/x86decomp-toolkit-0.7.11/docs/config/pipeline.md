# Pipeline

`$id: urn:x86decomp:schema:pipeline:1` — schema version 1.

Validated against `schemas/pipeline.schema.json`.

A pipeline defines an ordered DAG of stages that execute commands or evidence gates within a project.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `1` (const) | — |
| `pipeline_id` | string | minLength 1 — unique pipeline identifier |
| `project_root` | string | minLength 1 — path to the project root |
| `stages` | array of objects | minItems 1 |

---

## Optional fields

| Field | Type | Constraint |
|-------|------|------------|
| `created_at` | string | date-time format |

---

## Stage object

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `id` | string | yes | Pattern `^[A-Za-z0-9_-]+$` |
| `kind` | enum | yes | `command` or `evidence_gate` |
| `depends_on` | array of strings | no | Unique IDs of prerequisite stages |
| `command` | array of strings | yes if `command` | minItems 1 |
| `inputs` | array of strings | no | Unique file/directory paths |
| `outputs` | array of strings | no | Unique file/directory paths |
| `evidence_claim_ids` | array of strings | yes if `evidence_gate` | Unique claim IDs |
| `isolation` | enum | no | `local_bounded` or `container` |
| `container_image` | string or null | no | Container image name (when `isolation: container`) |
| `environment` | object (string→string) | no | Environment variables for the stage |
| `limits` | object (string→integer) | no | Resource limits (min 1 per key) |

### `kind`

| Value | Requires | Meaning |
|-------|----------|---------|
| `command` | `command` | Execute an external command |
| `evidence_gate` | `evidence_claim_ids` | Gate on evidence claims passing verification |

### `isolation`

| Value | Meaning |
|-------|---------|
| `local_bounded` | Run in a bounded local subprocess |
| `container` | Run in the specified `container_image` |

!!! warning
    When `isolation` is `container`, `container_image` must be a non-null string.

---

## Example

```json
{
  "schema_version": 1,
  "pipeline_id": "verify-match",
  "project_root": "/work/target-project",
  "created_at": "2026-07-01T12:00:00Z",
  "stages": [
    {
      "id": "compile",
      "kind": "command",
      "command": ["x86decomp", "compile", "--profile", "msvc6-x86-O2"],
      "inputs": ["src/matched"],
      "outputs": ["build/compiler"],
      "isolation": "local_bounded",
      "environment": {"PATH": "/usr/bin"}
    },
    {
      "id": "relink",
      "kind": "command",
      "depends_on": ["compile"],
      "command": ["x86decomp", "relink", "--manifest", "build/relink/manifest.json"],
      "inputs": ["build/compiler"],
      "outputs": ["build/relink"],
      "isolation": "local_bounded"
    },
    {
      "id": "evidence-check",
      "kind": "evidence_gate",
      "depends_on": ["relink"],
      "evidence_claim_ids": ["claim.byte-match.main", "claim.abi-compat.main"]
    }
  ]
}
```

!!! tip
    Stages execute in dependency order. `depends_on` creates a DAG — a stage runs only after all its dependencies complete successfully.

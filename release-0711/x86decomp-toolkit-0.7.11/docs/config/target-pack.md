# Target pack

`$id: urn:x86decomp:schema:target-pack:1` — schema version 1.

Validated against `schemas/target-pack.schema.json`.

A target pack is an immutable, target-specific record that captures identity, scope, architecture decisions, and a catalog of artifacts with verified hashes.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `1` (const) | — |
| `target_id` | string | minLength 1 |
| `name` | string | minLength 1 |
| `created_at` | string | date-time format |
| `architecture` | enum | `x86` or `x86_64` |
| `image_kind` | enum | `exe` or `dll` |
| `primary_image` | string | minLength 1 — path to the primary binary |
| `primary_sha256` | string | 64 lowercase hex chars |
| `default_modes` | `["matching", "functional"]` (const) | Always both modes |
| `scope` | object | Free-form scope definition |
| `decisions` | object | See examples/release/target-decisions.json in the toolkit distribution |
| `artifacts` | array of objects | minItems 1 |

### `primary_sha256`

Pattern: `^[0-9a-f]{64}$`. Must be lowercase hex.

---

## Artifacts array

Each artifact entry:

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `role` | string | yes | minLength 1 — semantic role (e.g. `primary_image`, `pdb`, `linker_map`) |
| `path` | string | yes | minLength 1 — file path |
| `sha256` | string | yes | 64 hex chars |
| `size` | integer | yes | minimum 1 — file size in bytes |

Common artifact role values include:

- `primary_image` — the main PE binary
- `reference_image` — a trusted reference copy
- `candidate_image` — a candidate reconstruction
- `pdb` — program database (debug symbols)
- `linker_map` — linker map file
- `coff_object` — individual COFF object file
- `static_library` — `.lib` archive
- `compiler_profile` — compiler profile used
- `image_profile` — image profile derived from the binary
- `source` — source code file

---

## Example

```json
{
  "schema_version": 1,
  "target_id": "example-game-exe",
  "name": "Example Game v1.0",
  "created_at": "2026-07-01T12:00:00Z",
  "architecture": "x86",
  "image_kind": "exe",
  "primary_image": "original/game.exe",
  "primary_sha256": "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789",
  "default_modes": ["matching", "functional"],
  "scope": {
    "functions": 1420,
    "sections": 4
  },
  "decisions": {
    "compiler_family": "msvc",
    "compiler_version": "12.00.8804",
    "linker_family": "msvc",
    "source_language": "c++"
  },
  "artifacts": [
    {
      "role": "primary_image",
      "path": "original/game.exe",
      "sha256": "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789",
      "size": 524288
    },
    {
      "role": "pdb",
      "path": "original/game.pdb",
      "sha256": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210",
      "size": 1048576
    }
  ]
}
```

!!! note
    The `decisions` object follows the `schemas/target-decisions.schema.json` schema. Accepted fields include `preferred_mode`, `compiler_family`, `compiler_version`, `linker_family`, `source_language`, `allow_host_execution`, and `target_description`.

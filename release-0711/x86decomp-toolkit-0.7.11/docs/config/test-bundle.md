# Test bundle

`$id: urn:x86decomp:schema:test-bundle:1` — schema version 1.

Validated against `schemas/test-bundle.schema.json`.

A test bundle is an authorized collection of artifacts — binaries, PDBs, maps, objects, source, and profiles — used for test-suite execution. Every bundle requires an authorization declaration that the user owns or is authorized to use the included artifacts.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `1` (const) | — |
| `authorization` | object | See below |
| `artifacts` | array of objects | minItems 1 |

---

## Optional fields

| Field | Type | Constraint |
|-------|------|------------|
| `name` | string | minLength 1 |
| `description` | string | — |
| `expected_architecture` | enum | `x86` or `x86_64` |

---

## `authorization` object

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `owner_or_authorized` | `true` (const) | yes | Must be `true` |
| `statement` | string | yes | minLength 1 — the authorization declaration text |

!!! warning
    `owner_or_authorized` is a const `true`. A test bundle cannot be loaded if this field is missing or `false`.

---

## Artifacts array

Each artifact entry:

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `path` | string | yes | minLength 1 |
| `role` | enum | yes | One of 11 allowed values (see below) |
| `sha256` | string (optional) | no | 64 hex chars (case-insensitive) |
| `description` | string (optional) | no | — |

### Allowed `role` values (11 total)

| Value | Meaning |
|-------|---------|
| `primary_image` | Main binary under test |
| `reference_image` | Trusted reference copy of the binary |
| `candidate_image` | Candidate reconstructed binary |
| `pdb` | Program database debug symbols |
| `linker_map` | Linker-generated map file |
| `coff_object` | Individual COFF object file |
| `static_library` | Static library archive (`.lib`) |
| `source` | Source code file |
| `compiler_profile` | Compiler profile JSON |
| `image_profile` | Image profile JSON |
| `documentation` | Supporting documentation |

---

## Example

```json
{
  "schema_version": 1,
  "name": "PE32 unit test corpus",
  "description": "x86 PE test binaries for matching validation",
  "expected_architecture": "x86",
  "authorization": {
    "owner_or_authorized": true,
    "statement": "I certify that I own or am authorized to use all files in this test bundle for decompilation research."
  },
  "artifacts": [
    {
      "path": "test-corpus/hello.exe",
      "role": "primary_image",
      "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    },
    {
      "path": "test-corpus/hello.pdb",
      "role": "pdb"
    },
    {
      "path": "test-corpus/hello.map",
      "role": "linker_map",
      "sha256": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
    },
    {
      "path": "test-corpus/hello.c",
      "role": "source",
      "description": "Original source for ground-truth comparison"
    }
  ]
}
```

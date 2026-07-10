---
title: schemas/synthetic-corpus.schema.json
description: Schema reference page for schemas/synthetic-corpus.schema.json.
---

# `schemas/synthetic-corpus.schema.json`

- SHA-256: `3c05d2c0a766021805afdd306d6a08068af6a24cdb0adb82fb3eca4d0f1d7c7d`
- Size: `2225` bytes
- Title: Deterministic synthetic source corpus
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:synthetic-corpus:1",
  "title": "Deterministic synthetic source corpus",
  "type": "object",
  "required": ["schema_version", "kind", "created_at", "seed", "cases_per_family", "families", "case_count", "cases", "truth_scope"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "synthetic_source_corpus"},
    "created_at": {"type": "string"},
    "seed": {"type": "integer", "minimum": 0},
    "cases_per_family": {"type": "integer", "minimum": 1, "maximum": 10000},
    "families": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["language", "name"],
        "properties": {
          "language": {"enum": ["c", "c++"]},
          "name": {"type": "string", "minLength": 1}
        },
        "additionalProperties": false
      }
    },
    "case_count": {"type": "integer", "minimum": 1},
    "cases": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id", "family", "language", "seed", "source", "source_sha256", "generator"],
        "properties": {
          "id": {"type": "string", "pattern": "^[A-Za-z_][A-Za-z0-9_]*$"},
          "family": {"type": "string", "minLength": 1},
          "language": {"enum": ["c", "c++"]},
          "seed": {"type": "integer", "minimum": 0},
          "source": {"type": "string", "minLength": 1},
          "source_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
          "generator": {"type": "string", "minLength": 1}
        },
        "additionalProperties": false
      }
    },
    "truth_scope": {
      "type": "object",
      "required": ["source_generation_reproducible", "compiler_execution_performed", "binary_equivalence_claimed", "original_source_recovery_claimed"],
      "properties": {
        "source_generation_reproducible": {"const": true},
        "compiler_execution_performed": {"const": false},
        "binary_equivalence_claimed": {"const": false},
        "original_source_recovery_claimed": {"const": false}
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

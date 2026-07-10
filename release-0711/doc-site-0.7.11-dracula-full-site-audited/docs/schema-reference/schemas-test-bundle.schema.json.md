---
title: schemas/test-bundle.schema.json
description: Schema reference page for schemas/test-bundle.schema.json.
---

# `schemas/test-bundle.schema.json`

- SHA-256: `398d162a3ccc9e3bd1e984af67efbfaf12a840f4013b406c0cf8d150f490deab`
- Size: `1451` bytes
- Title: x86decomp Authorized Static Test Bundle
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:test-bundle:1",
  "title": "x86decomp Authorized Static Test Bundle",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "authorization", "artifacts"],
  "properties": {
    "schema_version": {"const": 1},
    "name": {"type": "string", "minLength": 1},
    "description": {"type": "string"},
    "expected_architecture": {"enum": ["x86", "x86_64"]},
    "authorization": {
      "type": "object",
      "additionalProperties": false,
      "required": ["owner_or_authorized", "statement"],
      "properties": {
        "owner_or_authorized": {"const": true},
        "statement": {"type": "string", "minLength": 1}
      }
    },
    "artifacts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["path", "role"],
        "properties": {
          "path": {"type": "string", "minLength": 1},
          "role": {
            "enum": [
              "primary_image", "reference_image", "candidate_image", "pdb",
              "linker_map", "coff_object", "static_library", "source",
              "compiler_profile", "image_profile", "documentation"
            ]
          },
          "sha256": {"type": "string", "pattern": "^[0-9a-fA-F]{64}$"},
          "description": {"type": "string"}
        }
      }
    }
  }
}
```

---
title: schemas/target-pack.schema.json
description: Schema reference page for schemas/target-pack.schema.json.
---

# `schemas/target-pack.schema.json`

- SHA-256: `867b89f3738ff1310340d078c5ae530f0087277e96cd00106fa1275cd0bcc954`
- Size: `1400` bytes
- Title: urn:x86decomp:schema:target-pack:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:target-pack:1",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "target_id", "name", "created_at", "architecture", "image_kind", "primary_image", "primary_sha256", "default_modes", "scope", "decisions", "artifacts"],
  "properties": {
    "schema_version": {"const": 1},
    "target_id": {"type": "string", "minLength": 1},
    "name": {"type": "string", "minLength": 1},
    "created_at": {"type": "string", "format": "date-time"},
    "architecture": {"enum": ["x86", "x86_64"]},
    "image_kind": {"enum": ["exe", "dll"]},
    "primary_image": {"type": "string", "minLength": 1},
    "primary_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "default_modes": {"const": ["matching", "functional"]},
    "scope": {"type": "object"},
    "decisions": {"type": "object"},
    "artifacts": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["role", "path", "sha256", "size"],
        "properties": {
          "role": {"type": "string", "minLength": 1},
          "path": {"type": "string", "minLength": 1},
          "sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
          "size": {"type": "integer", "minimum": 1}
        }
      }
    }
  }
}
```

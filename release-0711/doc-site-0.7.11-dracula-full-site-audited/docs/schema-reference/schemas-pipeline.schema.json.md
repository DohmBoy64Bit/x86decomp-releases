---
title: schemas/pipeline.schema.json
description: Schema reference page for schemas/pipeline.schema.json.
---

# `schemas/pipeline.schema.json`

- SHA-256: `a9b7b790fb6c877370a4c61ecbdf0f92eac13d9aba389cc0ab8d8723aee92ca6`
- Size: `1850` bytes
- Title: urn:x86decomp:schema:pipeline:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:pipeline:1",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "pipeline_id", "project_root", "stages"],
  "properties": {
    "schema_version": {"const": 1},
    "pipeline_id": {"type": "string", "minLength": 1},
    "project_root": {"type": "string", "minLength": 1},
    "created_at": {"type": "string", "format": "date-time"},
    "stages": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["id", "kind"],
        "properties": {
          "id": {"type": "string", "pattern": "^[A-Za-z0-9_-]+$"},
          "kind": {"enum": ["command", "evidence_gate"]},
          "depends_on": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
          "command": {"type": "array", "items": {"type": "string", "minLength": 1}, "minItems": 1},
          "inputs": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
          "outputs": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
          "evidence_claim_ids": {"type": "array", "items": {"type": "string"}, "uniqueItems": true},
          "isolation": {"enum": ["local_bounded", "container"]},
          "container_image": {"type": ["string", "null"]},
          "environment": {"type": "object", "additionalProperties": {"type": "string"}},
          "limits": {"type": "object", "additionalProperties": {"type": "integer", "minimum": 1}}
        },
        "allOf": [
          {"if": {"properties": {"kind": {"const": "command"}}}, "then": {"required": ["command"]}},
          {"if": {"properties": {"kind": {"const": "evidence_gate"}}}, "then": {"required": ["evidence_claim_ids"]}}
        ]
      }
    }
  }
}
```

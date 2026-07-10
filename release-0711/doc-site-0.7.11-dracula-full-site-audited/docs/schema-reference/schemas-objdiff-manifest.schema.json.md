---
title: schemas/objdiff-manifest.schema.json
description: Schema reference page for schemas/objdiff-manifest.schema.json.
---

# `schemas/objdiff-manifest.schema.json`

- SHA-256: `2fe8f65399749687b2890cc643f474c0b8de221e90f6ae5013ce0d8b46590360`
- Size: `1006` bytes
- Title: objdiff external invocation manifest
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:objdiff-manifest:1",
  "title": "objdiff external invocation manifest",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "target", "candidate", "arguments"],
  "properties": {
    "schema_version": {"const": 1},
    "executable": {"type": "string", "minLength": 1},
    "target": {"type": "string", "minLength": 1},
    "candidate": {"type": "string", "minLength": 1},
    "arguments": {"type": "array", "minItems": 1, "items": {"type": "string"}},
    "output": {"type": "string", "minLength": 1},
    "output_format": {"enum": ["json", "text"]},
    "require_output": {"type": "boolean"},
    "timeout_seconds": {"type": "integer", "minimum": 1},
    "success_exit_codes": {"type": "array", "minItems": 1, "items": {"type": "integer"}},
    "inherit_environment": {"type": "boolean"},
    "environment": {"type": "object", "additionalProperties": {"type": "string"}}
  }
}
```

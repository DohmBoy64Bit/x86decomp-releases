---
title: schemas/relink-manifest.schema.json
description: Schema reference page for schemas/relink-manifest.schema.json.
---

# `schemas/relink-manifest.schema.json`

- SHA-256: `ca2b77b7be6b562589e841753a9afa8c6baf1fc7cf8c703409c90fc56507e890`
- Size: `1169` bytes
- Title: Manifest-driven full relink
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:relink-manifest:1",
  "title": "Manifest-driven full relink",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "linker",
    "objects",
    "output",
    "arguments",
    "environment",
    "timeout_seconds"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "linker": {
      "type": "string",
      "minLength": 1
    },
    "objects": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string"
      }
    },
    "output": {
      "type": "string",
      "minLength": 1
    },
    "arguments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string"
      },
      "contains": {
        "pattern": "\\{output\\}"
      }
    },
    "environment": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "inherit_environment": {
      "type": "boolean"
    },
    "timeout_seconds": {
      "type": "integer",
      "minimum": 1
    },
    "reference_image": {
      "type": "string"
    }
  }
}
```

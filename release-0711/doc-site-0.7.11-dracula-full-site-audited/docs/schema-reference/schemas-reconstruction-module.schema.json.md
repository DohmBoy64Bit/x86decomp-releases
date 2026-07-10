---
title: schemas/reconstruction/module.schema.json
description: Schema reference page for schemas/reconstruction/module.schema.json.
---

# `schemas/reconstruction/module.schema.json`

- SHA-256: `4aa87665cf31d30d9395bff7fb9388c9bd55257718808572669a874922436a4f`
- Size: `953` bytes
- Title: Recovered module hypothesis
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/module.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "confidence": {
      "maximum": 1,
      "minimum": 0,
      "type": "number"
    },
    "evidence": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "kind": {
      "enum": [
        "executable",
        "static-library",
        "shared-library",
        "resource",
        "support"
      ]
    },
    "module_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "name": {
      "minLength": 1,
      "type": "string"
    },
    "source_path": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "module_id",
    "name",
    "kind",
    "confidence",
    "evidence"
  ],
  "title": "Recovered module hypothesis",
  "type": "object"
}
```

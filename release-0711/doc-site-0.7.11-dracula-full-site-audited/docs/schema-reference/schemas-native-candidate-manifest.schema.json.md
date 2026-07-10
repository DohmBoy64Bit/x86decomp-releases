---
title: schemas/native/candidate-manifest.schema.json
description: Schema reference page for schemas/native/candidate-manifest.schema.json.
---

# `schemas/native/candidate-manifest.schema.json`

- SHA-256: `d3bad2e693b4b7d6e1c230d9e03ff775298273523c8b562d3b78400c13313029`
- Size: `750` bytes
- Title: x86decomp candidate-manifest
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/candidate-manifest.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "candidate_path": {
      "type": "string"
    },
    "function_id": {
      "type": "string"
    },
    "rva": {
      "oneOf": [
        {
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "slot_size": {
      "minimum": 1,
      "type": "integer"
    },
    "symbol": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "function_id",
    "rva",
    "slot_size",
    "candidate_path"
  ],
  "title": "x86decomp candidate-manifest",
  "type": "object"
}
```

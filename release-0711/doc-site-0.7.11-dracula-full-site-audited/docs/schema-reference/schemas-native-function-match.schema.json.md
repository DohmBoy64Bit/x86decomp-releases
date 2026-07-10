---
title: schemas/native/function-match.schema.json
description: Schema reference page for schemas/native/function-match.schema.json.
---

# `schemas/native/function-match.schema.json`

- SHA-256: `e598ca859f33c96b62fe8dac7fcf78ec77b53e4b8f178b9f19e1f288e2725cd1`
- Size: `754` bytes
- Title: x86decomp function-match
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/function-match.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "classification": {
      "enum": [
        "exact",
        "padding-normalized",
        "mismatch",
        "oversized"
      ]
    },
    "function_id": {
      "type": "string"
    },
    "replacement_safe": {
      "type": "boolean"
    },
    "rva": {
      "minimum": 0,
      "type": "integer"
    },
    "slot_size": {
      "minimum": 1,
      "type": "integer"
    }
  },
  "required": [
    "function_id",
    "rva",
    "slot_size",
    "classification",
    "replacement_safe"
  ],
  "title": "x86decomp function-match",
  "type": "object"
}
```

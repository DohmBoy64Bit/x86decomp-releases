---
title: schemas/native/function-slot.schema.json
description: Schema reference page for schemas/native/function-slot.schema.json.
---

# `schemas/native/function-slot.schema.json`

- SHA-256: `61bb10550455068b1c58073dfb30939aea8095cefbd775abab4d044efe9a2914`
- Size: `751` bytes
- Title: x86decomp function-slot
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/function-slot.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "body_size": {
      "minimum": 1,
      "type": "integer"
    },
    "classification": {
      "enum": [
        "exact",
        "padded",
        "overlap",
        "invalid-range"
      ]
    },
    "function_id": {
      "minLength": 1,
      "type": "string"
    },
    "rva": {
      "minimum": 0,
      "type": "integer"
    },
    "slot_size": {
      "type": "integer"
    }
  },
  "required": [
    "function_id",
    "rva",
    "body_size",
    "slot_size",
    "classification"
  ],
  "title": "x86decomp function-slot",
  "type": "object"
}
```

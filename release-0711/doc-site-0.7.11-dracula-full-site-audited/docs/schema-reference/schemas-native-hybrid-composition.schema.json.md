---
title: schemas/native/hybrid-composition.schema.json
description: Schema reference page for schemas/native/hybrid-composition.schema.json.
---

# `schemas/native/hybrid-composition.schema.json`

- SHA-256: `feb6682c1aa1ed0a3bc3c06230ce27f006641d96238050151ad22584eb02cb9d`
- Size: `599` bytes
- Title: x86decomp hybrid-composition
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/hybrid-composition.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "fallback_count": {
      "minimum": 0,
      "type": "integer"
    },
    "output": {
      "type": "string"
    },
    "promoted_count": {
      "minimum": 0,
      "type": "integer"
    },
    "run_id": {
      "type": "string"
    }
  },
  "required": [
    "run_id",
    "output",
    "promoted_count",
    "fallback_count"
  ],
  "title": "x86decomp hybrid-composition",
  "type": "object"
}
```

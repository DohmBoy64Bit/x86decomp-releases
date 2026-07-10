---
title: schemas/native/section-export.schema.json
description: Schema reference page for schemas/native/section-export.schema.json.
---

# `schemas/native/section-export.schema.json`

- SHA-256: `121ed87fe1b51a248b230acafd9780b96e74e01c72e9cba7fcd20fbb466eb317`
- Size: `451` bytes
- Title: x86decomp section-export
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/section-export.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "sections": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "source": {
      "type": "string"
    }
  },
  "required": [
    "source",
    "sections"
  ],
  "title": "x86decomp section-export",
  "type": "object"
}
```

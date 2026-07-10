---
title: schemas/native/patch-plan.schema.json
description: Schema reference page for schemas/native/patch-plan.schema.json.
---

# `schemas/native/patch-plan.schema.json`

- SHA-256: `90a1f06eaa3f6a3d6b235cc0439c57fec0187006ccc4c01b8fbb76571bb31958`
- Size: `982` bytes
- Title: x86decomp patch-plan
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/patch-plan.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "operations": {
      "items": {
        "properties": {
          "expected_hex": {
            "pattern": "^[0-9a-f]*$",
            "type": "string"
          },
          "offset": {
            "minimum": 0,
            "type": "integer"
          },
          "replacement_hex": {
            "pattern": "^[0-9a-f]*$",
            "type": "string"
          }
        },
        "required": [
          "offset",
          "expected_hex",
          "replacement_hex"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "original_path": {
      "type": "string"
    },
    "output_path": {
      "type": "string"
    }
  },
  "required": [
    "original_path",
    "output_path",
    "operations"
  ],
  "title": "x86decomp patch-plan",
  "type": "object"
}
```

---
title: schemas/native/runtime-validation.schema.json
description: Schema reference page for schemas/native/runtime-validation.schema.json.
---

# `schemas/native/runtime-validation.schema.json`

- SHA-256: `f314d1ae2b72314a6ebf6c6d2905a8eb2f314498f256f567e01ae08622da90f3`
- Size: `606` bytes
- Title: x86decomp runtime-validation
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/runtime-validation.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "checks": {
      "type": "object"
    },
    "image_path": {
      "type": "string"
    },
    "status": {
      "enum": [
        "passed",
        "failed",
        "blocked"
      ]
    },
    "validation_kind": {
      "type": "string"
    }
  },
  "required": [
    "image_path",
    "validation_kind",
    "status",
    "checks"
  ],
  "title": "x86decomp runtime-validation",
  "type": "object"
}
```

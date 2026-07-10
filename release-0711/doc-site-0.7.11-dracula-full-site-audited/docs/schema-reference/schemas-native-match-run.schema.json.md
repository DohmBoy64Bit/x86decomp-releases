---
title: schemas/native/match-run.schema.json
description: Schema reference page for schemas/native/match-run.schema.json.
---

# `schemas/native/match-run.schema.json`

- SHA-256: `7afbfb42c5995ff375a050c93bb119ce50f2a761220c610f2c1622f082c23fb5`
- Size: `468` bytes
- Title: x86decomp match-run
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/match-run.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "comparison_policy": {
      "enum": [
        "exact",
        "trailing-padding"
      ]
    },
    "original_path": {
      "type": "string"
    }
  },
  "required": [
    "original_path",
    "comparison_policy"
  ],
  "title": "x86decomp match-run",
  "type": "object"
}
```

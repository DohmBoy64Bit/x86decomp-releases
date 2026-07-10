---
title: schemas/native/staging-symbol.schema.json
description: Schema reference page for schemas/native/staging-symbol.schema.json.
---

# `schemas/native/staging-symbol.schema.json`

- SHA-256: `44b3ce02db0758435f6a230a9ad37bd00c3a6308bf71761836050e5c90c6c4d0`
- Size: `607` bytes
- Title: x86decomp staging-symbol
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/staging-symbol.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "declaration": {
      "type": "string"
    },
    "status": {
      "enum": [
        "proposed",
        "accepted",
        "rejected"
      ]
    },
    "symbol_kind": {
      "type": "string"
    },
    "symbol_name": {
      "type": "string"
    }
  },
  "required": [
    "symbol_name",
    "symbol_kind",
    "declaration",
    "status"
  ],
  "title": "x86decomp staging-symbol",
  "type": "object"
}
```

---
title: schemas/reconstruction/header.schema.json
description: Schema reference page for schemas/reconstruction/header.schema.json.
---

# `schemas/reconstruction/header.schema.json`

- SHA-256: `c878f851e64b11db9e0dad34785d5ef3ba3baa753e380af72f554fe44529a850`
- Size: `737` bytes
- Title: Recovered header contract
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/header.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "declarations": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "header_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "path": {
      "pattern": ".*\\.(h|hpp|hh)$",
      "type": "string"
    },
    "visibility": {
      "enum": [
        "public",
        "private",
        "internal"
      ]
    }
  },
  "required": [
    "header_id",
    "path",
    "visibility",
    "declarations"
  ],
  "title": "Recovered header contract",
  "type": "object"
}
```

---
title: schemas/reconstruction/library-match.schema.json
description: Schema reference page for schemas/reconstruction/library-match.schema.json.
---

# `schemas/reconstruction/library-match.schema.json`

- SHA-256: `cdf8967118c99e0f1d224829f1e3067a2b9db50f31ca945db68a3cec61b0f36e`
- Size: `1060` bytes
- Title: Static library recognition candidate
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/library-match.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "confidence": {
      "maximum": 1,
      "minimum": 0,
      "type": "number"
    },
    "disposition": {
      "enum": [
        "proposed",
        "accepted",
        "externalized",
        "reconstruct",
        "rejected"
      ]
    },
    "evidence": {
      "items": {
        "type": "object"
      },
      "minItems": 1,
      "type": "array"
    },
    "library_name": {
      "type": "string"
    },
    "match_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "subject_id": {
      "type": "string"
    },
    "version_range": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "match_id",
    "subject_id",
    "library_name",
    "confidence",
    "evidence",
    "disposition"
  ],
  "title": "Static library recognition candidate",
  "type": "object"
}
```

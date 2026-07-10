---
title: schemas/reconstruction/generated-test.schema.json
description: Schema reference page for schemas/reconstruction/generated-test.schema.json.
---

# `schemas/reconstruction/generated-test.schema.json`

- SHA-256: `8e99342ae82922d0c5c17c41e857074a5a2cec9b1269e23572aea09b5715a7b5`
- Size: `1117` bytes
- Title: Generated regression test
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/generated-test.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "content_sha256": {
      "pattern": "^[0-9a-f]{64}$",
      "type": "string"
    },
    "generated_test_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "name": {
      "minLength": 1,
      "type": "string"
    },
    "relative_path": {
      "minLength": 1,
      "type": "string"
    },
    "scope_id": {
      "minLength": 1,
      "type": "string"
    },
    "scope_kind": {
      "minLength": 1,
      "type": "string"
    },
    "test_kind": {
      "enum": [
        "unit",
        "differential",
        "abi",
        "serialization",
        "golden",
        "fuzz",
        "trace",
        "symbolic",
        "layout"
      ]
    }
  },
  "required": [
    "generated_test_id",
    "name",
    "scope_kind",
    "scope_id",
    "test_kind",
    "relative_path",
    "content_sha256"
  ],
  "title": "Generated regression test",
  "type": "object"
}
```

---
title: schemas/reconstruction/source-provenance.schema.json
description: Schema reference page for schemas/reconstruction/source-provenance.schema.json.
---

# `schemas/reconstruction/source-provenance.schema.json`

- SHA-256: `d80a00434549c01f14f1afa7c43cb65b9eb653808b42fb5fa10f25b1d7ac1b0c`
- Size: `1200` bytes
- Title: Source provenance record
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/source-provenance.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "address_end": {
      "minLength": 1,
      "type": "string"
    },
    "address_start": {
      "minLength": 1,
      "type": "string"
    },
    "binary_id": {
      "minLength": 1,
      "type": "string"
    },
    "confidence": {
      "maximum": 1,
      "minimum": 0,
      "type": "number"
    },
    "evidence": {
      "items": {
        "type": "object"
      },
      "minItems": 1,
      "type": "array"
    },
    "line_end": {
      "minimum": 1,
      "type": "integer"
    },
    "line_start": {
      "minimum": 1,
      "type": "integer"
    },
    "provenance_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "source_path": {
      "minLength": 1,
      "type": "string"
    }
  },
  "required": [
    "provenance_id",
    "source_path",
    "line_start",
    "line_end",
    "binary_id",
    "address_start",
    "address_end",
    "evidence",
    "confidence"
  ],
  "title": "Source provenance record",
  "type": "object"
}
```

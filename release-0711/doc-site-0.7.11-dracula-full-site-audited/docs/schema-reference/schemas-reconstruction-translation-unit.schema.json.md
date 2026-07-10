---
title: schemas/reconstruction/translation-unit.schema.json
description: Schema reference page for schemas/reconstruction/translation-unit.schema.json.
---

# `schemas/reconstruction/translation-unit.schema.json`

- SHA-256: `ea17fb7bfec69c8e9e3eb5d14179194acece94ba90d5e0ad76c5f3e653dca642`
- Size: `846` bytes
- Title: Translation unit hypothesis
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/translation-unit.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "confidence": {
      "maximum": 1,
      "minimum": 0,
      "type": "number"
    },
    "evidence": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "language": {
      "enum": [
        "c",
        "cpp",
        "asm",
        "resource"
      ]
    },
    "source_path": {
      "minLength": 1,
      "type": "string"
    },
    "unit_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    }
  },
  "required": [
    "unit_id",
    "source_path",
    "language",
    "confidence",
    "evidence"
  ],
  "title": "Translation unit hypothesis",
  "type": "object"
}
```

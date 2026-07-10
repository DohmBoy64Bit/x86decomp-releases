---
title: schemas/type-constraint.schema.json
description: Schema reference page for schemas/type-constraint.schema.json.
---

# `schemas/type-constraint.schema.json`

- SHA-256: `f98328b457deccc685ea8be764507320d5ff94deddb366e47c5018a678baa59d`
- Size: `1023` bytes
- Title: Type/ABI constraint record
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:type-constraint:1",
  "title": "Type/ABI constraint record",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "subject_entity",
    "relation",
    "object_value",
    "provenance",
    "status"
  ],
  "properties": {
    "constraint_id": {
      "type": "integer",
      "minimum": 1
    },
    "subject_entity": {
      "type": "string",
      "minLength": 1
    },
    "relation": {
      "type": "string",
      "minLength": 1
    },
    "object_value": {
      "type": "string",
      "minLength": 1
    },
    "provenance": {
      "type": "string",
      "minLength": 1
    },
    "evidence_id": {
      "type": [
        "string",
        "null"
      ]
    },
    "confidence": {
      "type": [
        "number",
        "null"
      ],
      "minimum": 0,
      "maximum": 1
    },
    "status": {
      "enum": [
        "candidate",
        "accepted",
        "rejected"
      ]
    }
  }
}
```

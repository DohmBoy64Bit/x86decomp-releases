---
title: schemas/governance/review.schema.json
description: Schema reference page for schemas/governance/review.schema.json.
---

# `schemas/governance/review.schema.json`

- SHA-256: `280cfe7963adcdcbbb3a1fde01b921cad82751d2240a4fcdaa9b9543db071bc2`
- Size: `778` bytes
- Title: review item
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "details": {
      "type": "object"
    },
    "kind": {
      "type": "string"
    },
    "locked": {
      "type": "boolean"
    },
    "priority": {
      "maximum": 100,
      "minimum": 0,
      "type": "integer"
    },
    "status": {
      "enum": [
        "open",
        "assigned",
        "accepted",
        "rejected",
        "needs_evidence",
        "superseded"
      ]
    },
    "subject_id": {
      "type": "string"
    },
    "summary": {
      "minLength": 1,
      "type": "string"
    }
  },
  "required": [
    "kind",
    "subject_id",
    "priority",
    "status",
    "summary"
  ],
  "title": "review item",
  "type": "object"
}
```

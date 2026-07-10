---
title: schemas/governance/candidate.schema.json
description: Schema reference page for schemas/governance/candidate.schema.json.
---

# `schemas/governance/candidate.schema.json`

- SHA-256: `db23f94af8b37ebdfff2798c271a0ef02ea9d77aae83fa8c8ebdab3d2f55ad67`
- Size: `716` bytes
- Title: candidate
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "branch_name": {
      "minLength": 1,
      "type": "string"
    },
    "evaluations": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "files": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "objective": {
      "type": "object"
    },
    "state": {
      "enum": [
        "active",
        "evaluating",
        "supported",
        "promoted",
        "discarded",
        "blocked"
      ]
    }
  },
  "required": [
    "branch_name",
    "state",
    "objective"
  ],
  "title": "candidate",
  "type": "object"
}
```

---
title: schemas/governance/campaign.schema.json
description: Schema reference page for schemas/governance/campaign.schema.json.
---

# `schemas/governance/campaign.schema.json`

- SHA-256: `df027ea63ef0017b5a9ecae133a21ab7fa13f68e00545529e8606b5f39d1f854`
- Size: `896` bytes
- Title: campaign
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "budget": {
      "additionalProperties": {
        "minimum": 0,
        "type": "integer"
      },
      "type": "object"
    },
    "goal": {
      "enum": [
        "recover_function",
        "recover_module",
        "behavioral_equivalence",
        "byte_identical",
        "types_and_symbols"
      ]
    },
    "policy": {
      "type": "object"
    },
    "status": {
      "enum": [
        "created",
        "running",
        "paused",
        "blocked",
        "completed",
        "stopped"
      ]
    },
    "used": {
      "additionalProperties": {
        "minimum": 0,
        "type": "integer"
      },
      "type": "object"
    }
  },
  "required": [
    "goal",
    "status",
    "budget",
    "used"
  ],
  "title": "campaign",
  "type": "object"
}
```

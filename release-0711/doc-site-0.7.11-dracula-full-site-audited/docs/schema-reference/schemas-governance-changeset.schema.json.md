---
title: schemas/governance/changeset.schema.json
description: Schema reference page for schemas/governance/changeset.schema.json.
---

# `schemas/governance/changeset.schema.json`

- SHA-256: `6788b90056dbf46cdaaaab292bdc6c3102e20ff47c790f131b47c15d08f5cbd3`
- Size: `715` bytes
- Title: changeset manifest
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "base_event_hash": {
      "type": [
        "string",
        "null"
      ]
    },
    "changeset_id": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "event_count": {
      "minimum": 0,
      "type": "integer"
    },
    "format": {
      "const": "x86decomp-governance-changeset-v1"
    },
    "tip_event_hash": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "format",
    "changeset_id",
    "base_event_hash",
    "tip_event_hash",
    "event_count"
  ],
  "title": "changeset manifest",
  "type": "object"
}
```

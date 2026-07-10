---
title: schemas/governance/hypothesis.schema.json
description: Schema reference page for schemas/governance/hypothesis.schema.json.
---

# `schemas/governance/hypothesis.schema.json`

- SHA-256: `1013bee5c093d4cf0e619dbcdc52a2b2ff79c0b768da9c699ad0483bfc283a83`
- Size: `929` bytes
- Title: hypothesis
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "confidence": {
      "maximum": 1,
      "minimum": 0,
      "type": "number"
    },
    "locked": {
      "type": "boolean"
    },
    "origin": {
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
    "state": {
      "enum": [
        "proposed",
        "scheduled",
        "testing",
        "supported",
        "contradicted",
        "accepted",
        "rejected",
        "superseded",
        "blocked"
      ]
    },
    "statement": {
      "minLength": 1,
      "type": "string"
    }
  },
  "required": [
    "statement",
    "scope_kind",
    "scope_id",
    "state",
    "confidence",
    "origin"
  ],
  "title": "hypothesis",
  "type": "object"
}
```

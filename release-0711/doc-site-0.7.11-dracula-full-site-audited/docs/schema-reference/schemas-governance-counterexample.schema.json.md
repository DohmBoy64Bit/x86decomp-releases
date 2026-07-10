---
title: schemas/governance/counterexample.schema.json
description: Schema reference page for schemas/governance/counterexample.schema.json.
---

# `schemas/governance/counterexample.schema.json`

- SHA-256: `0e2b706ed1bf89e6c07a483dd171dbb23fbac4f67c87ef1df16be6c2fe50d19c`
- Size: `757` bytes
- Title: counterexample
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "current_sha256": {
      "pattern": "^[a-f0-9]{64}$",
      "type": "string"
    },
    "predicate": {
      "type": "object"
    },
    "provenance": {
      "type": "object"
    },
    "scope_id": {
      "type": "string"
    },
    "scope_kind": {
      "type": "string"
    },
    "size_bytes": {
      "minimum": 1,
      "type": "integer"
    },
    "state": {
      "enum": [
        "recorded",
        "minimized",
        "regression"
      ]
    }
  },
  "required": [
    "scope_kind",
    "scope_id",
    "current_sha256",
    "size_bytes",
    "state",
    "predicate"
  ],
  "title": "counterexample",
  "type": "object"
}
```

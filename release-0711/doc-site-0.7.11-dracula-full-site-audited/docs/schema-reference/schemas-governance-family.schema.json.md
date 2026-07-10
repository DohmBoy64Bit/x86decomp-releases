---
title: schemas/governance/family.schema.json
description: Schema reference page for schemas/governance/family.schema.json.
---

# `schemas/governance/family.schema.json`

- SHA-256: `cd02347eefe68396b21d7ec5af6ef9c1554dd4715e962e302ece657cb0b851ed`
- Size: `668` bytes
- Title: binary family report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "correlations": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "family_id": {
      "type": "string"
    },
    "members": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "name": {
      "type": "string"
    },
    "non_claims": {
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [
    "family_id",
    "name",
    "members",
    "correlations",
    "non_claims"
  ],
  "title": "binary family report",
  "type": "object"
}
```

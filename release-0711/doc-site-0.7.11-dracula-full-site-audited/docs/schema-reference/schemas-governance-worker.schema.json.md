---
title: schemas/governance/worker.schema.json
description: Schema reference page for schemas/governance/worker.schema.json.
---

# `schemas/governance/worker.schema.json`

- SHA-256: `ca8f6768a4c7dfe89e80f2107c4bb43badde4d01d3ec6947ff001c9b207b403c`
- Size: `689` bytes
- Title: worker profile
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "capabilities": {
      "minProperties": 1,
      "type": "object"
    },
    "endpoint": {
      "type": [
        "string",
        "null"
      ]
    },
    "environment_sha256": {
      "pattern": "^[a-f0-9]{64}$",
      "type": [
        "string",
        "null"
      ]
    },
    "name": {
      "type": "string"
    },
    "status": {
      "enum": [
        "active",
        "draining",
        "offline",
        "unhealthy"
      ]
    }
  },
  "required": [
    "name",
    "status",
    "capabilities"
  ],
  "title": "worker profile",
  "type": "object"
}
```

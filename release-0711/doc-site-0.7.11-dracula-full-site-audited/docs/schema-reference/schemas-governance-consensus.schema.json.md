---
title: schemas/governance/consensus.schema.json
description: Schema reference page for schemas/governance/consensus.schema.json.
---

# `schemas/governance/consensus.schema.json`

- SHA-256: `f3edcf4a5962701cde7a0f4f483a19d49e9f5beea5e6a4dc3c643c9970ee9c43`
- Size: `851` bytes
- Title: consensus observation
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "adapter_name": {
      "type": "string"
    },
    "adapter_version": {
      "type": "string"
    },
    "confidence": {
      "maximum": 1,
      "minimum": 0,
      "type": "number"
    },
    "evidence_id": {
      "type": "string"
    },
    "independence_group": {
      "type": "string"
    },
    "property_name": {
      "type": "string"
    },
    "subject_id": {
      "type": "string"
    },
    "subject_kind": {
      "type": "string"
    },
    "value": {}
  },
  "required": [
    "subject_kind",
    "subject_id",
    "property_name",
    "value",
    "adapter_name",
    "adapter_version",
    "evidence_id",
    "independence_group",
    "confidence"
  ],
  "title": "consensus observation",
  "type": "object"
}
```

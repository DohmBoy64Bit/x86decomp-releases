---
title: schemas/governance/knowledge-graph.schema.json
description: Schema reference page for schemas/governance/knowledge-graph.schema.json.
---

# `schemas/governance/knowledge-graph.schema.json`

- SHA-256: `d1bc76932c0264e763eb4cdb47d46397ddf00bb57e1c240371ef42049631db28`
- Size: `697` bytes
- Title: knowledge graph impact
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "direction": {
      "enum": [
        "outbound",
        "inbound",
        "both"
      ]
    },
    "edges": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "max_depth": {
      "maximum": 64,
      "minimum": 0,
      "type": "integer"
    },
    "nodes": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "root": {
      "type": "string"
    }
  },
  "required": [
    "root",
    "direction",
    "max_depth",
    "nodes",
    "edges"
  ],
  "title": "knowledge graph impact",
  "type": "object"
}
```

---
title: schemas/mcp-mutation.schema.json
description: Schema reference page for schemas/mcp-mutation.schema.json.
---

# `schemas/mcp-mutation.schema.json`

- SHA-256: `64335798160269133e880d823f14de7f0cb4f2dafbf0c47526e24fb9fb16ea29`
- Size: `1155` bytes
- Title: Evidence-gated MCP mutation
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:mcp-mutation:1",
  "title": "Evidence-gated MCP mutation",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "created_at",
    "tool",
    "arguments",
    "rationale",
    "evidence_ids",
    "status",
    "approval_hash"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "tool": {
      "type": "string",
      "minLength": 1
    },
    "arguments": {
      "type": "object"
    },
    "rationale": {
      "type": "string",
      "minLength": 1
    },
    "evidence_ids": {
      "type": "array",
      "minItems": 1,
      "uniqueItems": true,
      "items": {
        "type": "string"
      }
    },
    "status": {
      "enum": [
        "proposed",
        "committed"
      ]
    },
    "approval_hash": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$"
    },
    "committed_at": {
      "type": "string",
      "format": "date-time"
    },
    "result": {
      "type": "object"
    }
  }
}
```

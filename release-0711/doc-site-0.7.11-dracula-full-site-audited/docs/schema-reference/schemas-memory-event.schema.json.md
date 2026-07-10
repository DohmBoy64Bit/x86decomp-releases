---
title: schemas/memory-event.schema.json
description: Schema reference page for schemas/memory-event.schema.json.
---

# `schemas/memory-event.schema.json`

- SHA-256: `d2f38971ac7dda92dda0564bb77bb4858160b5a342476d36fe52238eb5289e74`
- Size: `1300` bytes
- Title: x86decomp project memory event
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:memory-event:1",
  "title": "x86decomp project memory event",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "id",
    "sequence",
    "timestamp",
    "actor",
    "category",
    "summary",
    "details",
    "evidence_ids",
    "previous_hash",
    "event_hash"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "id": {
      "type": "string",
      "pattern": "^mem-[0-9a-f]{16}$"
    },
    "sequence": {
      "type": "integer",
      "minimum": 1
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "actor": {
      "type": "string",
      "minLength": 1
    },
    "category": {
      "type": "string",
      "minLength": 1
    },
    "summary": {
      "type": "string",
      "minLength": 1
    },
    "details": {
      "type": "object"
    },
    "evidence_ids": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      }
    },
    "previous_hash": {
      "type": [
        "string",
        "null"
      ],
      "pattern": "^[0-9a-f]{64}$"
    },
    "event_hash": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$"
    }
  }
}
```

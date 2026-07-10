---
title: schemas/reconstruction/semantic-changeset.schema.json
description: Schema reference page for schemas/reconstruction/semantic-changeset.schema.json.
---

# `schemas/reconstruction/semantic-changeset.schema.json`

- SHA-256: `2cc66c0075ba39a54d86a20ca3705d4656ce90e922ce5a8c0b9357db1bc27b28`
- Size: `936` bytes
- Title: Semantic changeset
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/semantic-changeset.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "base_audit_hash": {
      "pattern": "^[0-9a-f]{64}$",
      "type": [
        "string",
        "null"
      ]
    },
    "changeset_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "operations": {
      "items": {
        "required": [
          "kind",
          "subject_id"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "status": {
      "enum": [
        "draft",
        "merged",
        "conflicted",
        "applied",
        "rejected"
      ]
    }
  },
  "required": [
    "changeset_id",
    "name",
    "operations",
    "status"
  ],
  "title": "Semantic changeset",
  "type": "object"
}
```

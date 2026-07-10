---
title: schemas/claim.schema.json
description: Schema reference page for schemas/claim.schema.json.
---

# `schemas/claim.schema.json`

- SHA-256: `362341adcb81640a7839c77d37d7203b911e7e79655be6c0ab4115f460609532`
- Size: `1305` bytes
- Title: x86decomp claim
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:claim:1",
  "title": "x86decomp claim",
  "type": "object",
  "required": [
    "id",
    "subject",
    "predicate",
    "object",
    "state",
    "evidence_ids",
    "contradiction_ids",
    "notes",
    "created_at",
    "updated_at"
  ],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9][a-z0-9._:-]{2,127}$"
    },
    "subject": {
      "type": "string",
      "minLength": 1
    },
    "predicate": {
      "type": "string",
      "minLength": 1
    },
    "object": {
      "type": "string",
      "minLength": 1
    },
    "state": {
      "enum": [
        "proposed",
        "corroborated",
        "verified",
        "rejected"
      ]
    },
    "evidence_ids": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      }
    },
    "contradiction_ids": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      }
    },
    "notes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time"
    }
  }
}
```

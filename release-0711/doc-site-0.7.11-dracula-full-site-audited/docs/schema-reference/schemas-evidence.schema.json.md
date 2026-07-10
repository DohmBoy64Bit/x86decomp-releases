---
title: schemas/evidence.schema.json
description: Schema reference page for schemas/evidence.schema.json.
---

# `schemas/evidence.schema.json`

- SHA-256: `5c5199ae9f480dbbb28eb3ebd889a53a46c08535cabf346d3a0bf04f4a4aa7bd`
- Size: `1243` bytes
- Title: x86decomp evidence item
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:evidence:1",
  "title": "x86decomp evidence item",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "id",
    "kind",
    "source",
    "locator",
    "assertion",
    "independent_group",
    "digest_sha256",
    "observed_at",
    "metadata"
  ],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9][a-z0-9._:-]{2,127}$"
    },
    "kind": {
      "enum": [
        "binary_bytes",
        "static_analysis",
        "dynamic_trace",
        "compiler_output",
        "debug_symbol",
        "external_document",
        "human_review"
      ]
    },
    "source": {
      "type": "string",
      "minLength": 1
    },
    "locator": {
      "type": "string",
      "minLength": 1
    },
    "assertion": {
      "type": "string",
      "minLength": 1
    },
    "independent_group": {
      "type": "string",
      "minLength": 1
    },
    "digest_sha256": {
      "type": [
        "string",
        "null"
      ],
      "pattern": "^[0-9a-f]{64}$"
    },
    "observed_at": {
      "type": "string",
      "format": "date-time"
    },
    "metadata": {
      "type": "object"
    }
  }
}
```

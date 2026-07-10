---
title: schemas/benchmark-corpus.schema.json
description: Schema reference page for schemas/benchmark-corpus.schema.json.
---

# `schemas/benchmark-corpus.schema.json`

- SHA-256: `0081dd4d038287641f14ccd228dd0e824bff8bd3745f8251aaa0a94c1c61e36c`
- Size: `1048` bytes
- Title: Ground-truth benchmark corpus
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:benchmark-corpus:1",
  "title": "Ground-truth benchmark corpus",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "name",
    "cases"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "cases": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "id",
          "kind"
        ],
        "properties": {
          "id": {
            "type": "string"
          },
          "kind": {
            "enum": [
              "byte_pair",
              "pe_coff",
              "dynamic",
              "symbolic",
              "integration",
              "discovery_metrics"
            ]
          },
          "human_interventions": {
            "type": "integer",
            "minimum": 0
          }
        },
        "additionalProperties": true
      }
    }
  }
}
```

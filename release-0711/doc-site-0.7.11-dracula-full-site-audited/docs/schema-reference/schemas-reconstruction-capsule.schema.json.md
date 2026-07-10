---
title: schemas/reconstruction/capsule.schema.json
description: Schema reference page for schemas/reconstruction/capsule.schema.json.
---

# `schemas/reconstruction/capsule.schema.json`

- SHA-256: `c042105ec33667d5f67b4bd36311aa9c2989f97ef6c6c57cd5d0e634ada1437c`
- Size: `1066` bytes
- Title: Reconstruction capsule manifest
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/capsule.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "external_requirements": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "members": {
      "items": {
        "properties": {
          "path": {
            "type": "string"
          },
          "sha256": {
            "pattern": "^[0-9a-f]{64}$",
            "type": "string"
          },
          "size": {
            "minimum": 0,
            "type": "integer"
          }
        },
        "required": [
          "path",
          "sha256",
          "size"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "schema": {
      "const": "x86decomp.capsule.v1"
    },
    "toolkit_version": {
      "const": "0.7.11"
    }
  },
  "required": [
    "schema",
    "toolkit_version",
    "members",
    "external_requirements"
  ],
  "title": "Reconstruction capsule manifest",
  "type": "object"
}
```

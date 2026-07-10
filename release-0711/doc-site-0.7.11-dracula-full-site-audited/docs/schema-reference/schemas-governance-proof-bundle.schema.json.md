---
title: schemas/governance/proof-bundle.schema.json
description: Schema reference page for schemas/governance/proof-bundle.schema.json.
---

# `schemas/governance/proof-bundle.schema.json`

- SHA-256: `b169fcd67f41318514ea5984fa5715cab569020f56547ccb58f93a98679090c0`
- Size: `882` bytes
- Title: proof bundle manifest
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "audit_tip": {
      "type": [
        "string",
        "null"
      ]
    },
    "files": {
      "additionalProperties": {
        "additionalProperties": false,
        "properties": {
          "sha256": {
            "pattern": "^[a-f0-9]{64}$",
            "type": "string"
          },
          "size": {
            "minimum": 0,
            "type": "integer"
          }
        },
        "required": [
          "sha256",
          "size"
        ],
        "type": "object"
      },
      "type": "object"
    },
    "format": {
      "const": "x86decomp-proof-bundle-v1"
    },
    "release": {
      "const": "0.7.11"
    }
  },
  "required": [
    "format",
    "release",
    "files"
  ],
  "title": "proof bundle manifest",
  "type": "object"
}
```

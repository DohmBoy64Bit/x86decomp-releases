---
title: schemas/reconstruction/abi-contract.schema.json
description: Schema reference page for schemas/reconstruction/abi-contract.schema.json.
---

# `schemas/reconstruction/abi-contract.schema.json`

- SHA-256: `d2286943caed629e873a4107fcceb21f18b0759cfebd17b71f761af14e68e016`
- Size: `960` bytes
- Title: ABI contract
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/abi-contract.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "architecture": {
      "enum": [
        "x86",
        "x86_64"
      ]
    },
    "contract": {
      "type": "object"
    },
    "contract_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "evidence": {
      "items": {
        "type": "object"
      },
      "minItems": 1,
      "type": "array"
    },
    "subject_id": {
      "minLength": 1,
      "type": "string"
    },
    "subject_kind": {
      "enum": [
        "function",
        "module",
        "library",
        "executable",
        "interface"
      ]
    }
  },
  "required": [
    "contract_id",
    "subject_kind",
    "subject_id",
    "architecture",
    "contract",
    "evidence"
  ],
  "title": "ABI contract",
  "type": "object"
}
```

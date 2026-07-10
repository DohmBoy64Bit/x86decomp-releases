---
title: schemas/reconstruction/compatibility-shim.schema.json
description: Schema reference page for schemas/reconstruction/compatibility-shim.schema.json.
---

# `schemas/reconstruction/compatibility-shim.schema.json`

- SHA-256: `714bcc499ffc2db676e163a5886ce9ca4fca7df0b2382a94488c6dfc5a782926`
- Size: `864` bytes
- Title: Explicit compatibility shim
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/compatibility-shim.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "contract": {
      "type": "object"
    },
    "shim_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "shim_kind": {
      "enum": [
        "reimplemented",
        "wrapped",
        "translated",
        "assumption-dependent",
        "externally-supplied"
      ]
    },
    "source_path": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "subject_id": {
      "type": "string"
    }
  },
  "required": [
    "shim_id",
    "subject_id",
    "shim_kind",
    "source_path",
    "contract",
    "status"
  ],
  "title": "Explicit compatibility shim",
  "type": "object"
}
```

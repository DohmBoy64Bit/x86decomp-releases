---
title: schemas/native/boundary-finding.schema.json
description: Schema reference page for schemas/native/boundary-finding.schema.json.
---

# `schemas/native/boundary-finding.schema.json`

- SHA-256: `58d723eee6c5c374f78dcac68a23be5d0b60c6f002c3e8285d307eef496e74fc`
- Size: `539` bytes
- Title: x86decomp boundary-finding
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/boundary-finding.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "finding_kind": {
      "type": "string"
    },
    "function_id": {
      "type": "string"
    },
    "severity": {
      "enum": [
        "info",
        "warning",
        "error"
      ]
    }
  },
  "required": [
    "function_id",
    "finding_kind",
    "severity"
  ],
  "title": "x86decomp boundary-finding",
  "type": "object"
}
```

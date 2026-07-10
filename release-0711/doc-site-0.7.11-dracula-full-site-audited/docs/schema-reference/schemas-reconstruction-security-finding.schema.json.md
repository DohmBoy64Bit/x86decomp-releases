---
title: schemas/reconstruction/security-finding.schema.json
description: Schema reference page for schemas/reconstruction/security-finding.schema.json.
---

# `schemas/reconstruction/security-finding.schema.json`

- SHA-256: `9a4f8a220e2e2d1d7dbc8116968bf2752d57a5725e18673faf59a192ace1826e`
- Size: `945` bytes
- Title: Security finding
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/security-finding.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "evidence": {
      "items": {
        "type": "object"
      },
      "minItems": 1,
      "type": "array"
    },
    "finding_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "rule_id": {
      "type": "string"
    },
    "severity": {
      "enum": [
        "informational",
        "low",
        "medium",
        "high",
        "critical"
      ]
    },
    "status": {
      "type": "string"
    },
    "subject_id": {
      "type": "string"
    },
    "summary": {
      "type": "string"
    }
  },
  "required": [
    "finding_id",
    "rule_id",
    "severity",
    "subject_id",
    "summary",
    "evidence",
    "status"
  ],
  "title": "Security finding",
  "type": "object"
}
```

---
title: schemas/symbolic-report.schema.json
description: Schema reference page for schemas/symbolic-report.schema.json.
---

# `schemas/symbolic-report.schema.json`

- SHA-256: `cc596ec7c42bc74e7810dbf52bf50cba2d17375e9438f0a3fcbb3dae67a88e29`
- Size: `523` bytes
- Title: Bounded symbolic comparison report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:symbolic-report:1",
  "title": "Bounded symbolic comparison report",
  "type": "object",
  "required": [
    "schema_version",
    "equivalent_within_model",
    "scope_statement"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "equivalent_within_model": {
      "type": "boolean"
    },
    "scope_statement": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": true
}
```

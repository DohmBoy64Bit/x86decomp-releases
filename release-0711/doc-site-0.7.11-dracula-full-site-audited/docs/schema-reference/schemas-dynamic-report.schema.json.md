---
title: schemas/dynamic-report.schema.json
description: Schema reference page for schemas/dynamic-report.schema.json.
---

# `schemas/dynamic-report.schema.json`

- SHA-256: `1af7c179c9d4fedbf542c098eab126d556fc8345a464176d211640f391effce0`
- Size: `647` bytes
- Title: Bounded Unicorn differential report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:dynamic-report:1",
  "title": "Bounded Unicorn differential report",
  "type": "object",
  "required": [
    "schema_version",
    "equivalent_for_harness",
    "target",
    "candidate",
    "scope_statement"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "equivalent_for_harness": {
      "type": "boolean"
    },
    "target": {
      "type": "object"
    },
    "candidate": {
      "type": "object"
    },
    "scope_statement": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": true
}
```

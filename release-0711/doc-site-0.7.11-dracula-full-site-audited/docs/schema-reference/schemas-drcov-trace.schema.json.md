---
title: schemas/drcov-trace.schema.json
description: Schema reference page for schemas/drcov-trace.schema.json.
---

# `schemas/drcov-trace.schema.json`

- SHA-256: `aedc8ab92612b4b325552d3de98da9d04e2e4c3aa2bb2ab319e20f85616cfe7f`
- Size: `1164` bytes
- Title: Normalized DynamoRIO drcov text trace
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:drcov-trace:1",
  "title": "Normalized DynamoRIO drcov text trace",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "kind",
    "source",
    "source_sha256",
    "drcov_version",
    "modules",
    "basic_blocks",
    "unique_basic_blocks"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "kind": {
      "const": "dynamorio_drcov_text"
    },
    "source": {
      "type": "string"
    },
    "source_sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$"
    },
    "drcov_version": {
      "type": "string"
    },
    "drcov_flavor": {
      "type": [
        "string",
        "null"
      ]
    },
    "module_table_version": {
      "type": [
        "integer",
        "null"
      ]
    },
    "modules": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "basic_blocks": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "unique_basic_blocks": {
      "type": "integer",
      "minimum": 0
    }
  }
}
```

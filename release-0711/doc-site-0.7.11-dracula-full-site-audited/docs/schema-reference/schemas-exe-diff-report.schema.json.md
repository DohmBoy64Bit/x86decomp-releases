---
title: schemas/exe-diff-report.schema.json
description: Schema reference page for schemas/exe-diff-report.schema.json.
---

# `schemas/exe-diff-report.schema.json`

- SHA-256: `3bfb70b7158750523074f638ff5955cc519097a37543f9f097909f4576373b50`
- Size: `1581` bytes
- Title: PE function to COFF symbol comparison
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:exe-diff-report:2",
  "title": "PE function to COFF symbol comparison",
  "type": "object",
  "required": [
    "schema_version",
    "classification",
    "pe",
    "coff",
    "normalization_masks",
    "raw_byte_comparison",
    "normalized_byte_comparison",
    "semantic_equivalence_claimed"
  ],
  "properties": {
    "schema_version": {
      "const": 2
    },
    "classification": {
      "enum": [
        "byte_matched",
        "relocation_normalized_match",
        "instruction_similar",
        "mismatch"
      ]
    },
    "pe": {
      "type": "object"
    },
    "coff": {
      "type": "object"
    },
    "normalization_masks": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "raw_byte_comparison": {
      "type": "object"
    },
    "normalized_byte_comparison": {
      "type": "object"
    },
    "instruction_comparison": {
      "type": [
        "object",
        "null"
      ]
    },
    "instruction_comparison_error": {
      "type": [
        "string",
        "null"
      ]
    },
    "semantic_equivalence_claimed": {
      "const": false
    },
    "limitations": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "kind": {
      "const": "pe_function_vs_coff_symbol"
    },
    "architecture": {
      "enum": [
        "x86",
        "x86_64"
      ]
    }
  },
  "additionalProperties": true
}
```

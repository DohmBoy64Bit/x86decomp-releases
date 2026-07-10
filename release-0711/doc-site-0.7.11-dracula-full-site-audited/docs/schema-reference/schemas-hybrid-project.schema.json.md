---
title: schemas/hybrid-project.schema.json
description: Schema reference page for schemas/hybrid-project.schema.json.
---

# `schemas/hybrid-project.schema.json`

- SHA-256: `c72692b4469f7ba92b2945968974d495371e2c0f03ad438c970418c3ce31d9b0`
- Size: `1940` bytes
- Title: Continuously buildable hybrid project
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:hybrid-project:1",
  "title": "Continuously buildable hybrid project",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "created_at",
    "project_root",
    "architecture",
    "functions",
    "build"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "project_root": {
      "type": "string"
    },
    "architecture": {
      "enum": [
        "x86",
        "x86_64"
      ]
    },
    "functions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "function_id",
          "rva",
          "symbol",
          "assembly",
          "active_build_form",
          "source_of_truth"
        ],
        "properties": {
          "function_id": {
            "type": "string"
          },
          "rva": {
            "type": "integer"
          },
          "symbol": {
            "type": "string"
          },
          "assembly": {
            "type": "string"
          },
          "staging_source": {
            "type": [
              "string",
              "null"
            ]
          },
          "active_build_form": {
            "enum": [
              "assembly",
              "matched_source",
              "functional_source"
            ]
          },
          "source_of_truth": {
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    },
    "build": {
      "type": "object",
      "required": [
        "kind",
        "object_count"
      ],
      "properties": {
        "kind": {
          "type": "string"
        },
        "object_count": {
          "type": "integer",
          "minimum": 0
        }
      },
      "additionalProperties": false
    }
  }
}
```

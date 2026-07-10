---
title: schemas/compiler-ground-truth.schema.json
description: Schema reference page for schemas/compiler-ground-truth.schema.json.
---

# `schemas/compiler-ground-truth.schema.json`

- SHA-256: `1f8d15358ce71168a0f7c4d61ba7ad9db1ef12b534b27444bdda1f77f96392a2`
- Size: `1514` bytes
- Title: Compiler ground-truth corpus manifest
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:compiler-ground-truth:1",
  "title": "Compiler ground-truth corpus manifest",
  "type": "object",
  "required": ["schema_version", "compilers", "cases"],
  "properties": {
    "schema_version": {"const": 1},
    "timeout_seconds": {"type": "integer", "minimum": 1},
    "compilers": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object", "required": ["id", "executable", "base_args"],
        "properties": {
          "id": {"type": "string"}, "executable": {"type": "string"},
          "base_args": {"type": "array", "items": {"type": "string"}},
          "version_args": {"type": "array", "items": {"type": "string"}},
          "environment": {"type": "object", "additionalProperties": {"type": "string"}},
          "inherit_environment": {"type": "boolean"}
        }, "additionalProperties": false
      }
    },
    "flag_matrix": {"type": "object"},
    "cases": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object", "required": ["id", "source"],
        "properties": {
          "id": {"type": "string"}, "source": {"type": "string"},
          "compilers": {"type": "array", "items": {"type": "string"}},
          "arguments": {"type": "array", "items": {"type": "string"}},
          "flag_matrix": {"type": "object"}, "output_name": {"type": "string"}
        }, "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

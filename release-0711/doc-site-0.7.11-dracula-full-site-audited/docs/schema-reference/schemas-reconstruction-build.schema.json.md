---
title: schemas/reconstruction/build.schema.json
description: Schema reference page for schemas/reconstruction/build.schema.json.
---

# `schemas/reconstruction/build.schema.json`

- SHA-256: `647d938812825abaa84206de119ebc4a18d8fad70a4f50121f990a4af2571dd0`
- Size: `773` bytes
- Title: Build reconstruction contract
- Type: `object`

```json
{
  "$id": "https://x86decomp.dev/schemas/reconstruction/build.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "build_id": {
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$",
      "type": "string"
    },
    "generator": {
      "enum": [
        "cmake",
        "make",
        "ninja",
        "msvc-project",
        "response-file"
      ]
    },
    "mode": {
      "enum": [
        "historical",
        "portable"
      ]
    },
    "targets": {
      "items": {
        "type": "object"
      },
      "type": "array"
    }
  },
  "required": [
    "build_id",
    "mode",
    "generator",
    "targets"
  ],
  "title": "Build reconstruction contract",
  "type": "object"
}
```

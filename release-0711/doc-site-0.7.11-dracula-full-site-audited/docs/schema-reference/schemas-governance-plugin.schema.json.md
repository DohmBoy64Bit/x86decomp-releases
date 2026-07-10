---
title: schemas/governance/plugin.schema.json
description: Schema reference page for schemas/governance/plugin.schema.json.
---

# `schemas/governance/plugin.schema.json`

- SHA-256: `1fb5e12f5c8eb5408dea6372c5442273b1694559dc9c09784bbca4309dbf5fd2`
- Size: `701` bytes
- Title: plugin manifest
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "api_version": {
      "const": "1"
    },
    "capabilities": {
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array",
      "uniqueItems": true
    },
    "executable": {
      "minLength": 1,
      "type": "string"
    },
    "name": {
      "minLength": 1,
      "type": "string"
    },
    "version": {
      "minLength": 1,
      "type": "string"
    }
  },
  "required": [
    "name",
    "version",
    "api_version",
    "executable",
    "capabilities"
  ],
  "title": "plugin manifest",
  "type": "object"
}
```

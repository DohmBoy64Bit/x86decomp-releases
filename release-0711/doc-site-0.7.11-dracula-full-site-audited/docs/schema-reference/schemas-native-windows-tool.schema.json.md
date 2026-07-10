---
title: schemas/native/windows-tool.schema.json
description: Schema reference page for schemas/native/windows-tool.schema.json.
---

# `schemas/native/windows-tool.schema.json`

- SHA-256: `22af6f0e3266250f1c741e95e231c4ee3d62fd3944e0000e6ab6e652089906e0`
- Size: `484` bytes
- Title: x86decomp windows-tool
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/windows-tool.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "available": {
      "type": "boolean"
    },
    "path": {
      "type": [
        "string",
        "null"
      ]
    },
    "tool_name": {
      "type": "string"
    }
  },
  "required": [
    "tool_name",
    "available"
  ],
  "title": "x86decomp windows-tool",
  "type": "object"
}
```

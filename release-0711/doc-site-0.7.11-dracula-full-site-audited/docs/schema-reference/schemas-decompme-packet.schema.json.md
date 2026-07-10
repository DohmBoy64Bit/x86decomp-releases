---
title: schemas/decompme-packet.schema.json
description: Schema reference page for schemas/decompme-packet.schema.json.
---

# `schemas/decompme-packet.schema.json`

- SHA-256: `65cd0a5d3197e6de85ec46c8eb372a387102192d9341ee252a7f40ca83b91704`
- Size: `1160` bytes
- Title: Local decomp.me-style function packet
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:decompme-packet:1",
  "title": "Local decomp.me-style function packet",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "created_at", "kind", "function_id", "source_artifact", "output_directory", "files", "uploaded", "limitations"],
  "properties": {
    "schema_version": {"const": 1},
    "created_at": {"type": "string"},
    "kind": {"const": "local_decompme_function_packet"},
    "function_id": {"type": "string", "pattern": "^pe-rva:[0-9A-Fa-f]{8}$"},
    "source_artifact": {"type": "string"},
    "output_directory": {"type": "string"},
    "files": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["path", "sha256", "size"],
        "properties": {
          "path": {"type": "string"},
          "sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
          "size": {"type": "integer", "minimum": 0}
        }
      }
    },
    "uploaded": {"const": false},
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

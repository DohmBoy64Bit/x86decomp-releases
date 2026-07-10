---
title: schemas/coff-archive.schema.json
description: Schema reference page for schemas/coff-archive.schema.json.
---

# `schemas/coff-archive.schema.json`

- SHA-256: `5f5a43f1ce6ae1221df24107f7b9db057156731736ff4aad5c81c93a73abaab3`
- Size: `2079` bytes
- Title: x86decomp COFF Archive Inspection
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:coff-archive:1",
  "title": "x86decomp COFF Archive Inspection",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "format", "source_path", "source_sha256", "member_count", "members", "linker_symbols"],
  "properties": {
    "schema_version": {"const": 1},
    "format": {"const": "coff_archive"},
    "source_path": {"type": ["string", "null"]},
    "source_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "member_count": {"type": "integer", "minimum": 0},
    "members": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["index", "header_offset", "data_offset", "name", "size", "timestamp", "user_id", "group_id", "mode", "kind", "sha256"],
        "properties": {
          "index": {"type": "integer", "minimum": 0},
          "header_offset": {"type": "integer", "minimum": 0},
          "data_offset": {"type": "integer", "minimum": 0},
          "name": {"type": "string"},
          "size": {"type": "integer", "minimum": 0},
          "timestamp": {"type": ["integer", "null"]},
          "user_id": {"type": ["integer", "null"]},
          "group_id": {"type": ["integer", "null"]},
          "mode": {"type": ["integer", "null"]},
          "kind": {"enum": ["linker_member", "longnames", "coff_object", "import_object", "unknown"]},
          "sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
          "import_object": {"type": "object"},
          "coff": {"type": "object"}
        },
        "additionalProperties": false
      }
    },
    "linker_symbols": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["name", "member_header_offset", "linker_member_index"],
        "properties": {
          "name": {"type": "string"},
          "member_header_offset": {"type": "integer", "minimum": 0},
          "linker_member_index": {"type": "integer", "minimum": 0}
        }
      }
    }
  }
}
```

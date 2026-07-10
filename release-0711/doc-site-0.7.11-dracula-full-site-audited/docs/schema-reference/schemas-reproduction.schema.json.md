---
title: schemas/reproduction.schema.json
description: Schema reference page for schemas/reproduction.schema.json.
---

# `schemas/reproduction.schema.json`

- SHA-256: `aea350be271c7795406a2dd55096775e9d0b531215e05f43b75a9c6b5bd98281`
- Size: `854` bytes
- Title: urn:x86decomp:schema:reproduction:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:reproduction:1",
  "type": "object",
  "required": ["schema_version", "project_id", "project_schema_version", "binary", "critical_files", "tools"],
  "properties": {
    "schema_version": {"const": 1},
    "created_at": {"type": "string"},
    "project_id": {"type": "string"},
    "project_schema_version": {"type": "integer"},
    "toolkit_release": {"type": "string"},
    "host": {"type": "object"},
    "binary": {"type": "object"},
    "critical_files": {"type": "array", "items": {"type": "object"}},
    "tools": {"type": "object"},
    "content_store": {"type": ["object", "null"]},
    "project_check": {"type": "object"},
    "target_pack_check": {"type": ["object", "null"]},
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

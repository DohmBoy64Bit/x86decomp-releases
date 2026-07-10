---
title: schemas/assembly/symbol-map.schema.json
description: Schema reference page for schemas/assembly/symbol-map.schema.json.
---

# `schemas/assembly/symbol-map.schema.json`

- SHA-256: `ddacd944e055f1b3e9e902199252271944479183e3cfc77cbf11ff9443b867d6`
- Size: `926` bytes
- Title: v0.7.11 original-RVA symbol map
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://x86decomp.local/schemas/assembly/symbol-map.schema.json",
  "title": "v0.7.11 original-RVA symbol map",
  "type": "object",
  "additionalProperties": {
    "oneOf": [
      {"type": "integer", "minimum": 0},
      {"type": "string", "pattern": "^(0[xX][0-9a-fA-F]+|[0-9]+)$"},
      {
        "type": "object",
        "required": ["rva"],
        "properties": {
          "rva": {"oneOf": [{"type": "integer", "minimum": 0}, {"type": "string", "pattern": "^(0[xX][0-9a-fA-F]+|[0-9]+)$"}]},
          "section_rva": {"oneOf": [{"type": "null"}, {"type": "integer", "minimum": 0}, {"type": "string", "pattern": "^(0[xX][0-9a-fA-F]+|[0-9]+)$"}]},
          "section_index": {"oneOf": [{"type": "null"}, {"type": "integer", "minimum": 1}]},
          "kind": {"type": "string"}
        },
        "additionalProperties": false
      }
    ]
  }
}
```

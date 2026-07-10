---
title: schemas/linker-layout.schema.json
description: Schema reference page for schemas/linker-layout.schema.json.
---

# `schemas/linker-layout.schema.json`

- SHA-256: `a8faf6022c8b70e04c3375d47a480b9a811e72edd55ea7e0ec4e80a77a8ca934`
- Size: `769` bytes
- Title: Linker layout reconstruction report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:linker-layout:1",
  "title": "Linker layout reconstruction report",
  "type": "object",
  "required": ["schema_version", "kind", "image", "map", "contributions", "unresolved"],
  "properties": {
    "schema_version": {"const": 1}, "kind": {"const": "linker_layout_reconstruction"},
    "image": {"type": "object"}, "map": {"type": "object"},
    "contributions": {"type": "array", "items": {"type": "object"}},
    "comdat_resolution": {"type": ["object", "null"]},
    "unresolved": {"type": "array", "items": {"type": "string"}},
    "object_order_evidenced": {"type": "boolean"}, "complete_original_layout_claimed": {"type": "boolean"}
  }, "additionalProperties": true
}
```

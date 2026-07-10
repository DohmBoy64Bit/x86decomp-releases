---
title: schemas/linker-reconstruction-plan.schema.json
description: Schema reference page for schemas/linker-reconstruction-plan.schema.json.
---

# `schemas/linker-reconstruction-plan.schema.json`

- SHA-256: `1d6fadf9737abed4d02cc90d3859898785edf62d3909c39fe893c8841c57f504`
- Size: `1234` bytes
- Title: urn:x86decomp:schema:linker-reconstruction-plan:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:linker-reconstruction-plan:1",
  "type": "object",
  "required": ["schema_version", "kind", "reference_image", "map", "objects", "sections", "placements", "comdat_resolution", "relink_manifest", "unresolved", "ready_for_relink"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "linker_reconstruction_plan"},
    "created_at": {"type": "string"},
    "reference_image": {"type": "object"},
    "map": {"type": "object"},
    "objects": {"type": "array", "items": {"type": "object"}},
    "libraries": {"type": "array", "items": {"type": "object"}},
    "archives": {"type": "array", "items": {"type": "object"}},
    "sections": {"type": "array", "items": {"type": "object"}},
    "placements": {"type": "array", "items": {"type": "object"}},
    "comdat_resolution": {"type": "object"},
    "linker": {"type": "string"},
    "relink_manifest": {"type": "object"},
    "unresolved": {"type": "array", "items": {"type": "string"}},
    "ready_for_relink": {"type": "boolean"},
    "complete_original_link_command_claimed": {"const": false},
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

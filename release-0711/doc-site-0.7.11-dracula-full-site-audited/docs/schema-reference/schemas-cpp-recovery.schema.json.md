---
title: schemas/cpp-recovery.schema.json
description: Schema reference page for schemas/cpp-recovery.schema.json.
---

# `schemas/cpp-recovery.schema.json`

- SHA-256: `9eda5eb04cdd6404ed82077dab0b1f2668f3682b33f864fec3c7348439515d8a`
- Size: `932` bytes
- Title: urn:x86decomp:schema:cpp-recovery:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:cpp-recovery:1",
  "type": "object",
  "required": ["schema_version", "kind", "classes", "vtable_groups", "adjustor_thunk_candidates", "counts", "claims", "limitations"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "bounded_cpp_recovery"},
    "created_at": {"type": "string"},
    "image": {"type": ["object", "null"]},
    "metadata_source": {"type": "string"},
    "classes": {"type": "array", "items": {"type": "object"}},
    "vtable_groups": {"type": "array", "items": {"type": "object"}},
    "adjustor_thunk_candidates": {"type": "array", "items": {"type": "object"}},
    "static_initializer_order_evidence": {"type": "array", "items": {"type": "object"}},
    "counts": {"type": "object"},
    "claims": {"type": "object"},
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

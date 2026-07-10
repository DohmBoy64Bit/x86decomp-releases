---
title: schemas/msvc-metadata.schema.json
description: Schema reference page for schemas/msvc-metadata.schema.json.
---

# `schemas/msvc-metadata.schema.json`

- SHA-256: `84d0b6bc880ab47954f951a4eed4db317c14ee33ed5cdbe0ee098ce61c1d6273`
- Size: `688` bytes
- Title: Bounded MSVC metadata analysis report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:msvc-metadata:1",
  "title": "Bounded MSVC metadata analysis report",
  "type": "object",
  "required": ["schema_version", "kind", "image", "rtti", "exceptions", "tls", "static_initializers", "source_level_recovery_claimed"],
  "properties": {
    "schema_version": {"const": 1}, "kind": {"const": "msvc_metadata_analysis"},
    "image": {"type": "object"}, "rtti": {"type": "object"}, "exceptions": {"type": "object"},
    "tls": {"type": ["object", "null"]}, "static_initializers": {"type": "object"},
    "source_level_recovery_claimed": {"const": false}
  }, "additionalProperties": true
}
```

---
title: schemas/comdat-resolution.schema.json
description: Schema reference page for schemas/comdat-resolution.schema.json.
---

# `schemas/comdat-resolution.schema.json`

- SHA-256: `01fd177dfa983202ca8770e7985aa623e166fd22c20fdecc1d3d37f9cbfe0aae`
- Size: `579` bytes
- Title: COFF COMDAT resolution report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:comdat-resolution:1",
  "title": "COFF COMDAT resolution report",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "valid", "winners", "discarded", "conflicts"],
  "properties": {
    "schema_version": {"const": 1},
    "valid": {"type": "boolean"},
    "winners": {"type": "array", "items": {"type": "object"}},
    "discarded": {"type": "array", "items": {"type": "object"}},
    "conflicts": {"type": "array", "items": {"type": "object"}}
  }
}
```

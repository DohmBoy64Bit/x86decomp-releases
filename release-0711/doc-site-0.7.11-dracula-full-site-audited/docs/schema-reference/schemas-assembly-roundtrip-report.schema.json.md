---
title: schemas/assembly/roundtrip-report.schema.json
description: Schema reference page for schemas/assembly/roundtrip-report.schema.json.
---

# `schemas/assembly/roundtrip-report.schema.json`

- SHA-256: `fd727824f525c79838ba3366ea7a3651490cd270d9e267734efca7d9223a3650`
- Size: `941` bytes
- Title: v0.7.11 mnemonic round-trip report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://x86decomp.local/schemas/assembly/roundtrip-report.schema.json",
  "title": "v0.7.11 mnemonic round-trip report",
  "type": "object",
  "required": ["source", "object", "symbol", "rva", "architecture", "input_sha256", "resolved_sha256", "exact_match", "classification"],
  "properties": {
    "source": {"type": "string", "minLength": 1},
    "object": {"type": "string", "minLength": 1},
    "symbol": {"type": "string", "minLength": 1},
    "rva": {"type": "integer", "minimum": 0},
    "architecture": {"enum": ["x86", "x86_64"]},
    "input_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "resolved_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "exact_match": {"type": "boolean"},
    "classification": {"enum": ["exact", "mismatch"]},
    "semantic_equivalence_claimed": {"const": false}
  },
  "additionalProperties": true
}
```

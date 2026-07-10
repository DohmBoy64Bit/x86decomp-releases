---
title: schemas/release-gate.schema.json
description: Schema reference page for schemas/release-gate.schema.json.
---

# `schemas/release-gate.schema.json`

- SHA-256: `50e1f5a6cb46b67f833c881a7f025be5c7c047c1f23c3607608488afe17256cd`
- Size: `701` bytes
- Title: urn:x86decomp:schema:release-gate:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:release-gate:1",
  "type": "object",
  "required": ["schema_version", "kind", "created_at", "project_root", "checks", "requirements", "failures", "passed", "truth_statement"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "target_release_gate"},
    "created_at": {"type": "string"},
    "project_root": {"type": "string"},
    "checks": {"type": "object"},
    "requirements": {"type": "object"},
    "failures": {"type": "array", "items": {"type": "string"}},
    "passed": {"type": "boolean"},
    "truth_statement": {"type": "string"}
  },
  "additionalProperties": true
}
```

---
title: schemas/convergence-report.schema.json
description: Schema reference page for schemas/convergence-report.schema.json.
---

# `schemas/convergence-report.schema.json`

- SHA-256: `ace195921a16f72366e2920e6e2ce4e464b51f665d4d12ff5117dbea49119185`
- Size: `1059` bytes
- Title: urn:x86decomp:schema:convergence-report:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:convergence-report:1",
  "type": "object",
  "required": ["schema_version", "kind", "reference_sha256", "candidate_sha256", "image_match", "totals", "sections", "next_actions", "complete", "normalized_complete"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "image_convergence_report"},
    "created_at": {"type": "string"},
    "reference_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "candidate_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "image_match": {"type": "object"},
    "totals": {"type": "object"},
    "sections": {"type": "array", "items": {"type": "object"}},
    "next_actions": {"type": "array", "items": {"type": "object"}},
    "delta_from_previous": {"type": ["object", "null"]},
    "complete": {"type": "boolean"},
    "normalized_complete": {"type": "boolean"},
    "root_cause_claimed": {"const": false},
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

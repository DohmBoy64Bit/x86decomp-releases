---
title: schemas/project-template.schema.json
description: Schema reference page for schemas/project-template.schema.json.
---

# `schemas/project-template.schema.json`

- SHA-256: `1bf881ea328d3a6c00d727c0cbe1e47763726e70362a085354178add994458ce`
- Size: `1609` bytes
- Title: Grounded x86decomp project-template contract
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:project-template:1",
  "title": "Grounded x86decomp project-template contract",
  "type": "object",
  "required": ["schema_version", "created_at", "target_id", "architecture", "image_kind", "selected_modes", "matching", "functional", "artifact_roles", "blockers", "truth_policy"],
  "properties": {
    "schema_version": {"const": 1},
    "created_at": {"type": "string"},
    "target_id": {"type": "string", "minLength": 1},
    "architecture": {"enum": ["x86", "x86_64"]},
    "image_kind": {"enum": ["exe", "dll"]},
    "selected_modes": {"type": "array", "minItems": 1, "uniqueItems": true, "items": {"enum": ["matching", "functional"]}},
    "source_language_decision": {"type": "string"},
    "source_language_candidates": {"type": "array", "items": {"type": "object"}},
    "matching": {"type": "object"},
    "functional": {"type": "object"},
    "artifact_roles": {"type": "array", "items": {"type": "string"}},
    "blockers": {"type": "array", "items": {"type": "object", "required": ["area", "fact", "reason"]}},
    "truth_policy": {
      "type": "object",
      "required": ["generated_source_claimed", "compiler_inferred_without_evidence", "linker_inferred_without_evidence", "unknowns_preserved"],
      "properties": {
        "generated_source_claimed": {"const": false},
        "compiler_inferred_without_evidence": {"const": false},
        "linker_inferred_without_evidence": {"const": false},
        "unknowns_preserved": {"const": true}
      }
    }
  },
  "additionalProperties": true
}
```

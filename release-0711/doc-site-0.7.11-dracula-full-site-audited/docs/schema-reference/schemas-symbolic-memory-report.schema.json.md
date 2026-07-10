---
title: schemas/symbolic-memory-report.schema.json
description: Schema reference page for schemas/symbolic-memory-report.schema.json.
---

# `schemas/symbolic-memory-report.schema.json`

- SHA-256: `5e17dedb1bedf6581662f4cced118e40b8075957a161daea2abfab778d0298ba`
- Size: `1042` bytes
- Title: Bounded angr symbolic memory-alias comparison
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:symbolic-memory-report:1",
  "title": "Bounded angr symbolic memory-alias comparison",
  "type": "object",
  "additionalProperties": true,
  "required": ["schema_version", "kind", "architecture", "harness", "target_execution", "candidate_execution", "equivalent_within_completed_model", "scope_statement", "universal_equivalence_claimed"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "angr_memory_alias_comparison"},
    "architecture": {"enum": ["x86", "x86_64"]},
    "target_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "candidate_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "harness": {"type": "object"},
    "target_execution": {"type": "object"},
    "candidate_execution": {"type": "object"},
    "equivalent_within_completed_model": {"type": "boolean"},
    "scope_statement": {"type": "string", "minLength": 1},
    "universal_equivalence_claimed": {"const": false}
  }
}
```

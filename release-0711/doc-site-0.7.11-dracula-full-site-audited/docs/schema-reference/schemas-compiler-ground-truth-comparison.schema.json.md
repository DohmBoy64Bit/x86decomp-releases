---
title: schemas/compiler-ground-truth-comparison.schema.json
description: Schema reference page for schemas/compiler-ground-truth-comparison.schema.json.
---

# `schemas/compiler-ground-truth-comparison.schema.json`

- SHA-256: `1ea55d940c62d4e60487f74ac4d9756e4ff4c7cb2c39c9dd629b1d4150646dfb`
- Size: `708` bytes
- Title: Compiler/version ground-truth corpus comparison
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:compiler-ground-truth-comparison:1",
  "title": "Compiler/version ground-truth corpus comparison",
  "type": "object",
  "additionalProperties": true,
  "required": ["schema_version", "kind", "reports", "comparisons", "summary", "semantic_equivalence_claimed"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "compiler_ground_truth_comparison"},
    "reports": {"type": "array", "minItems": 2, "items": {"type": "object"}},
    "comparisons": {"type": "array", "items": {"type": "object"}},
    "summary": {"type": "object"},
    "semantic_equivalence_claimed": {"const": false}
  }
}
```

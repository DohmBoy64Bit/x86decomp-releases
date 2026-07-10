---
title: schemas/image-match-report.schema.json
description: Schema reference page for schemas/image-match-report.schema.json.
---

# `schemas/image-match-report.schema.json`

- SHA-256: `f81f81c2581b2941b9a3850aa2d296957e1d14de2ad3d8ee92839b34ccfadc23`
- Size: `1063` bytes
- Title: Target-specific whole-image match report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:image-match-report:1",
  "title": "Target-specific whole-image match report",
  "type": "object",
  "additionalProperties": true,
  "required": ["schema_version", "kind", "reference", "candidate", "profile", "raw_exact_match", "normalized_match", "sections", "classification", "universal_equivalence_claimed"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "target_specific_whole_image_match"},
    "reference": {"type": "object"},
    "candidate": {"type": "object"},
    "profile": {"type": "object"},
    "raw_exact_match": {"type": "boolean"},
    "raw_mismatch_count": {"type": "integer", "minimum": 0},
    "normalized_match": {"type": "boolean"},
    "normalized_mismatch_count": {"type": "integer", "minimum": 0},
    "sections": {"type": "array", "items": {"type": "object"}},
    "classification": {"enum": ["byte_identical", "profile_normalized_match", "different"]},
    "universal_equivalence_claimed": {"const": false}
  }
}
```

---
title: schemas/verification.schema.json
description: Schema reference page for schemas/verification.schema.json.
---

# `schemas/verification.schema.json`

- SHA-256: `a70e3422e6b0bec967695257c7b66d44f17a0cfe3f15d99799eb1c038ccb7fa0`
- Size: `1495` bytes
- Title: x86decomp byte verification report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:verification:1",
  "title": "x86decomp byte verification report",
  "type": "object",
  "required": [
    "schema_version",
    "created_at",
    "equal",
    "target_size",
    "candidate_size",
    "target_sha256",
    "candidate_sha256",
    "matching_prefix_bytes",
    "matching_suffix_bytes",
    "sequence_similarity",
    "reported_mismatches",
    "mismatch_report_truncated",
    "semantic_equivalence_claimed"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "equal": {
      "type": "boolean"
    },
    "target_size": {
      "type": "integer",
      "minimum": 0
    },
    "candidate_size": {
      "type": "integer",
      "minimum": 0
    },
    "target_sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$"
    },
    "candidate_sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$"
    },
    "matching_prefix_bytes": {
      "type": "integer",
      "minimum": 0
    },
    "matching_suffix_bytes": {
      "type": "integer",
      "minimum": 0
    },
    "sequence_similarity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "reported_mismatches": {
      "type": "array"
    },
    "mismatch_report_truncated": {
      "type": "boolean"
    },
    "semantic_equivalence_claimed": {
      "const": false
    }
  }
}
```

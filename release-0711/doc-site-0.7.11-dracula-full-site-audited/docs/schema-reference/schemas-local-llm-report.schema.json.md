---
title: schemas/local-llm/report.schema.json
description: Schema reference page for schemas/local-llm/report.schema.json.
---

# `schemas/local-llm/report.schema.json`

- SHA-256: `d61c0308354431848f281d3c62cd32b39c9d61277492bee480a02276e5ad6ac0`
- Size: `2379` bytes
- Title: Local LLM exact byte-match report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://x86decomp.local/schemas/local-llm/report.schema.json",
  "title": "Local LLM exact byte-match report",
  "type": "object",
  "required": [
    "schema_version",
    "kind",
    "created_at",
    "status",
    "profile",
    "compiler_profile",
    "job",
    "attempt_limit",
    "attempt_count",
    "attempts",
    "accepted",
    "claim",
    "limitations"
  ],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "local_llm_byte_match"},
    "created_at": {"type": "string"},
    "status": {"enum": ["byte_matched", "blocked", "exhausted"]},
    "profile": {"type": "object"},
    "compiler_profile": {"type": "object"},
    "job": {"type": "object"},
    "attempt_limit": {"type": "integer", "minimum": 1, "maximum": 32},
    "attempt_count": {"type": "integer", "minimum": 0, "maximum": 32},
    "attempts": {"type": "array", "items": {"type": "object"}},
    "accepted": {
      "oneOf": [
        {"type": "null"},
        {
          "type": "object",
          "required": [
            "attempt",
            "source",
            "source_sha256",
            "object",
            "object_sha256",
            "resolved_bytes",
            "resolved_sha256",
            "target_sha256",
            "byte_identical",
            "unresolved_relocations"
          ],
          "properties": {
            "attempt": {"type": "integer", "minimum": 1},
            "source": {"type": "string"},
            "source_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "object": {"type": "string"},
            "object_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "resolved_bytes": {"type": "string"},
            "resolved_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "target_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "byte_identical": {"const": true},
            "unresolved_relocations": {"const": 0}
          }
        }
      ]
    },
    "claim": {"type": "string"},
    "limitations": {"type": "array", "items": {"type": "string"}}
  },
  "allOf": [
    {
      "if": {"properties": {"status": {"const": "byte_matched"}}},
      "then": {"properties": {"accepted": {"type": "object"}}},
      "else": {"properties": {"accepted": {"type": "null"}}}
    }
  ]
}
```

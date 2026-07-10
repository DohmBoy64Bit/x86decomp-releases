---
title: schemas/dependency-audit.schema.json
description: Schema reference page for schemas/dependency-audit.schema.json.
---

# `schemas/dependency-audit.schema.json`

- SHA-256: `2eef4097789050d846536b406ccd7b9e8e639467bdf1ca530045fcc6050c8ee2`
- Size: `1002` bytes
- Title: x86decomp dependency vulnerability audit
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:dependency-audit:1",
  "title": "x86decomp dependency vulnerability audit",
  "type": "object",
  "required": ["schema_version", "kind", "created_at", "tool", "tool_sha256", "return_code", "dependency_count", "vulnerability_count", "vulnerabilities", "passed", "raw_report"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "python_dependency_vulnerability_audit"},
    "created_at": {"type": "string"},
    "tool": {"type": "string"},
    "tool_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "return_code": {"type": "integer", "enum": [0, 1]},
    "dependency_count": {"type": "integer", "minimum": 0},
    "vulnerability_count": {"type": "integer", "minimum": 0},
    "vulnerabilities": {"type": "array", "items": {"type": "object"}},
    "passed": {"type": "boolean"},
    "stderr": {"type": "string"},
    "raw_report": {}
  },
  "additionalProperties": true
}
```

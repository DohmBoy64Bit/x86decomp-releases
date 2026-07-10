---
title: schemas/security-audit.schema.json
description: Schema reference page for schemas/security-audit.schema.json.
---

# `schemas/security-audit.schema.json`

- SHA-256: `d62a14bd5c6d796dd52aee929ccfdf8e1265f825167070c8ffd680321a00b637`
- Size: `821` bytes
- Title: urn:x86decomp:schema:security-audit:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:security-audit:1",
  "type": "object",
  "required": ["schema_version", "kind", "root", "file_count", "findings", "severity_counts", "passed", "vulnerability_database_checked"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "source_security_audit"},
    "created_at": {"type": "string"},
    "root": {"type": "string"},
    "file_count": {"type": "integer", "minimum": 0},
    "total_bytes": {"type": "integer", "minimum": 0},
    "findings": {"type": "array", "items": {"type": "object"}},
    "severity_counts": {"type": "object"},
    "passed": {"type": "boolean"},
    "vulnerability_database_checked": {"const": false},
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

---
title: schemas/test-bundle-report.schema.json
description: Schema reference page for schemas/test-bundle-report.schema.json.
---

# `schemas/test-bundle-report.schema.json`

- SHA-256: `482f5b618cd46eb5e815392f2655bb9fe4f3683e1f5122b8f7ab0ea69f8a2820`
- Size: `863` bytes
- Title: x86decomp Static Test Bundle Report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:test-bundle-report:1",
  "title": "x86decomp Static Test Bundle Report",
  "type": "object",
  "required": ["schema_version", "kind", "archive", "bundle", "artifacts", "analyses", "errors", "static_analysis_only", "supplied_code_executed", "passed"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "static_test_bundle_report"},
    "created_at": {"type": "string"},
    "archive": {"type": "object"},
    "bundle": {"type": "object"},
    "artifacts": {"type": "array"},
    "analyses": {"type": "object"},
    "errors": {"type": "array"},
    "static_analysis_only": {"const": true},
    "supplied_code_executed": {"const": false},
    "passed": {"type": "boolean"},
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

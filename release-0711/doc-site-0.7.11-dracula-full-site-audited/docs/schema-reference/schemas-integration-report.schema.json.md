---
title: schemas/integration-report.schema.json
description: Schema reference page for schemas/integration-report.schema.json.
---

# `schemas/integration-report.schema.json`

- SHA-256: `4732a3a8f4038739f46c7b7b74b20999c68d9f637bac783a53b03eee91e91d1a`
- Size: `856` bytes
- Title: Bounded integration comparison report
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:integration-report:1",
  "title": "Bounded integration comparison report",
  "type": "object",
  "additionalProperties": true,
  "required": ["schema_version", "created_at", "kind", "execution", "scenario_count", "passed_count", "failed_count", "all_scenarios_equivalent", "scenarios", "limitations"],
  "properties": {
    "schema_version": {"const": 1},
    "kind": {"const": "integration_scenarios"},
    "scenario_count": {"type": "integer", "minimum": 1},
    "passed_count": {"type": "integer", "minimum": 0},
    "failed_count": {"type": "integer", "minimum": 0},
    "all_scenarios_equivalent": {"type": "boolean"},
    "scenarios": {"type": "array", "minItems": 1},
    "limitations": {"type": "array", "minItems": 1, "items": {"type": "string"}}
  }
}
```

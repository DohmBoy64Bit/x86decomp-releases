---
title: schemas/target-decisions.schema.json
description: Schema reference page for schemas/target-decisions.schema.json.
---

# `schemas/target-decisions.schema.json`

- SHA-256: `647192549c5e079a02e597648a0d3d2ade5078866f869b7e0da34324b5976ed6`
- Size: `850` bytes
- Title: Operator-confirmed target decisions
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:target-decisions:1",
  "title": "Operator-confirmed target decisions",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "preferred_mode",
    "compiler_family",
    "compiler_version",
    "linker_family",
    "source_language",
    "allow_host_execution",
    "target_description"
  ],
  "properties": {
    "preferred_mode": {"enum": ["matching", "functional", "both"]},
    "compiler_family": {"type": "string", "minLength": 1},
    "compiler_version": {"type": "string", "minLength": 1},
    "linker_family": {"type": "string", "minLength": 1},
    "source_language": {"enum": ["unknown", "c", "c++", "mixed"]},
    "allow_host_execution": {"type": "boolean"},
    "target_description": {"type": "string", "minLength": 1}
  }
}
```

---
title: schemas/execution-harness.schema.json
description: Schema reference page for schemas/execution-harness.schema.json.
---

# `schemas/execution-harness.schema.json`

- SHA-256: `2ec27dc202dcf7ab923c646c71e30769b0c18527aaf2e6ba44e70536574e4f68`
- Size: `1621` bytes
- Title: Bounded Unicorn execution harness
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:execution-harness:1",
  "title": "Bounded Unicorn execution harness",
  "type": "object",
  "additionalProperties": false,
  "required": ["architecture"],
  "properties": {
    "architecture": {"enum": ["x86", "x86_64"]},
    "code_base": {"type": "integer", "minimum": 1},
    "stack_base": {"type": "integer", "minimum": 1},
    "stack_size": {"type": "integer", "minimum": 4096},
    "sentinel_address": {"type": "integer", "minimum": 1},
    "max_instructions": {"type": "integer", "minimum": 1},
    "timeout_ms": {"type": "integer", "minimum": 1},
    "registers": {"type": "object", "additionalProperties": {"type": "integer"}},
    "stack_arguments_hex": {"type": "string", "pattern": "^(?:[0-9a-fA-F]{2})*$"},
    "memory": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["address"],
        "properties": {
          "address": {"type": "integer", "minimum": 0},
          "data_hex": {"type": "string", "pattern": "^(?:[0-9a-fA-F]{2})*$"},
          "size": {"type": "integer", "minimum": 1}
        }
      }
    },
    "observe_registers": {"type": "array", "items": {"type": "string"}},
    "observe_memory": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["address", "size"],
        "properties": {"address": {"type": "integer", "minimum": 0}, "size": {"type": "integer", "minimum": 1}}
      }
    },
    "stubs": {"type": "object", "additionalProperties": {"type": "object", "additionalProperties": {"type": "integer"}}}
  }
}
```

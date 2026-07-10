---
title: schemas/symbolic-memory-harness.schema.json
description: Schema reference page for schemas/symbolic-memory-harness.schema.json.
---

# `schemas/symbolic-memory-harness.schema.json`

- SHA-256: `e7ce53b843c172758fc086503e040cd1c60a3836f528b2c8396a7e77ab7c200a`
- Size: `1762` bytes
- Title: Bounded symbolic memory and alias harness
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:symbolic-memory-harness:1",
  "title": "Bounded symbolic memory and alias harness",
  "type": "object",
  "required": ["architecture", "regions"],
  "properties": {
    "architecture": {"enum": ["x86", "x86_64"]},
    "regions": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object",
        "required": ["name", "pointer_register", "size"],
        "properties": {
          "name": {"type": "string", "minLength": 1},
          "pointer_register": {"type": "string", "minLength": 1},
          "size": {"type": "integer", "minimum": 1, "maximum": 1048576},
          "alignment": {"type": "integer", "minimum": 1},
          "initial": {"type": "string"}
        },
        "additionalProperties": false
      }
    },
    "alias_constraints": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["left", "right", "relation"],
        "properties": {
          "left": {"type": "string"}, "right": {"type": "string"},
          "relation": {"enum": ["equal", "distinct", "disjoint", "may_alias"]}
        },
        "additionalProperties": false
      }
    },
    "observe_memory": {"type": "array", "items": {"type": "object"}},
    "input_registers": {"type": "array", "items": {"type": "string"}},
    "output_registers": {"type": "array", "items": {"type": "string"}},
    "stack_argument_words": {"type": "integer", "minimum": 0},
    "alias_slots": {"type": "integer", "minimum": 1, "maximum": 32},
    "slot_stride": {"type": "integer", "minimum": 1},
    "max_steps": {"type": "integer", "minimum": 1},
    "max_paths": {"type": "integer", "minimum": 1}
  },
  "additionalProperties": false
}
```

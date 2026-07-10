---
title: schemas/abi-contract.schema.json
description: Schema reference page for schemas/abi-contract.schema.json.
---

# `schemas/abi-contract.schema.json`

- SHA-256: `536e89f5ab760329f3799138b17c8a321170fc1fc729528d97b7f75d4af96c76`
- Size: `919` bytes
- Title: x86decomp ABI contract
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:abi-contract:1",
  "title": "x86decomp ABI contract",
  "type": "object",
  "additionalProperties": false,
  "required": ["architecture", "convention"],
  "properties": {
    "architecture": {"enum": ["x86", "x86_64"]},
    "convention": {"enum": ["cdecl", "stdcall", "thiscall", "fastcall", "vectorcall", "unknown"]},
    "stack_argument_bytes": {"type": ["integer", "null"], "minimum": 0},
    "callee_stack_cleanup": {"type": ["integer", "null"], "minimum": 0},
    "variadic": {"type": "boolean"},
    "this_register": {"type": ["string", "null"]},
    "register_arguments": {"type": "array", "items": {"type": "string"}},
    "return_registers": {"type": "array", "items": {"type": "string"}},
    "structure_return": {"type": "boolean"},
    "floating_point": {"enum": ["x87", "sse", "mixed", "none", "unknown"]}
  }
}
```

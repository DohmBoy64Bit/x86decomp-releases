---
title: schemas/assembly/asm-function.schema.json
description: Schema reference page for schemas/assembly/asm-function.schema.json.
---

# `schemas/assembly/asm-function.schema.json`

- SHA-256: `5203c2e7147c3d4a5b57d7f481e62a341c8a5a49aa6534c27350c51b67f49f4b`
- Size: `1284` bytes
- Title: v0.7.11 function assembly result
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://x86decomp.local/schemas/assembly/asm-function.schema.json",
  "title": "v0.7.11 function assembly result",
  "type": "object",
  "required": ["function_id", "symbol", "rva", "format", "classification", "exact_match", "input_sha256", "source_sha256"],
  "properties": {
    "function_id": {"type": "string", "minLength": 1},
    "symbol": {"type": "string", "minLength": 1},
    "rva": {"type": "integer", "minimum": 0},
    "format": {"enum": ["bytes", "annotated", "mnemonic"]},
    "classification": {"enum": ["byte-form", "annotated-byte-form", "fully-mnemonic", "mixed-mnemonic-byte", "byte-form-fallback"]},
    "exact_match": {"type": "boolean"},
    "instruction_count": {"type": "integer", "minimum": 0},
    "mnemonic_count": {"type": "integer", "minimum": 0},
    "byte_escape_count": {"type": "integer", "minimum": 0},
    "relocation_count": {"type": "integer", "minimum": 0},
    "resolved_relocation_count": {"type": "integer", "minimum": 0},
    "unresolved_relocation_count": {"type": "integer", "minimum": 0},
    "input_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "source_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"}
  },
  "additionalProperties": true
}
```

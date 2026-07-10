---
title: schemas/assembly/asm-run.schema.json
description: Schema reference page for schemas/assembly/asm-run.schema.json.
---

# `schemas/assembly/asm-run.schema.json`

- SHA-256: `da6ccd5588a1e5a2324c9e99e4ac21bc9246d7393c3042e5436ee5a40ba98736`
- Size: `581` bytes
- Title: v0.7.11 assembly run
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://x86decomp.local/schemas/assembly/asm-run.schema.json",
  "title": "v0.7.11 assembly run",
  "type": "object",
  "required": ["run_id", "asm_format", "architecture", "status", "summary"],
  "properties": {
    "run_id": {"type": "string", "minLength": 1},
    "asm_format": {"enum": ["bytes", "annotated", "mnemonic"]},
    "architecture": {"enum": ["x86", "x86_64"]},
    "status": {"enum": ["running", "completed", "failed"]},
    "summary": {"type": "object"}
  },
  "additionalProperties": true
}
```

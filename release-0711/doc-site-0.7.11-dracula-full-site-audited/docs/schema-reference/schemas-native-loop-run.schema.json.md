---
title: schemas/native/loop-run.schema.json
description: Schema reference page for schemas/native/loop-run.schema.json.
---

# `schemas/native/loop-run.schema.json`

- SHA-256: `de5d1a277444c3ea53ae0c4860d1a7978b478893fb893cf4c1ba1fca4a11b038`
- Size: `609` bytes
- Title: x86decomp loop-run
- Type: `object`

```json
{
  "$id": "https://x86decomp.invalid/schemas/native/loop-run.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": true,
  "properties": {
    "candidate_path": {
      "type": "string"
    },
    "compile_command": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "function_id": {
      "type": "string"
    },
    "source_path": {
      "type": "string"
    }
  },
  "required": [
    "function_id",
    "source_path",
    "compile_command",
    "candidate_path"
  ],
  "title": "x86decomp loop-run",
  "type": "object"
}
```

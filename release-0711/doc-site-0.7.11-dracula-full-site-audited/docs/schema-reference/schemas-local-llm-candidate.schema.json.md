---
title: schemas/local-llm/candidate.schema.json
description: Schema reference page for schemas/local-llm/candidate.schema.json.
---

# `schemas/local-llm/candidate.schema.json`

- SHA-256: `cadff624248794b1841a55fd49f2f980658a442d046530c183ec0c89d44d99ab`
- Size: `530` bytes
- Title: Local LLM C proposal response
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://x86decomp.local/schemas/local-llm/candidate.schema.json",
  "title": "Local LLM C proposal response",
  "type": "object",
  "additionalProperties": false,
  "required": ["status", "c_source", "assumptions", "rationale"],
  "properties": {
    "status": {"enum": ["proposed", "blocked"]},
    "c_source": {"type": "string"},
    "assumptions": {"type": "array", "items": {"type": "string"}},
    "rationale": {"type": "string", "minLength": 1}
  }
}
```

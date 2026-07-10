---
title: schemas/worker-report.schema.json
description: Schema reference page for schemas/worker-report.schema.json.
---

# `schemas/worker-report.schema.json`

- SHA-256: `f4fee8d629c5e963519a4f5ab25c4bb0856592421ee218fe7d047b5ebe089b3c`
- Size: `1073` bytes
- Title: urn:x86decomp:schema:worker-report:1
- Type: `object`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:x86decomp:schema:worker-report:1",
  "type": "object",
  "required": ["schema_version", "status", "command", "isolation", "isolation_strength", "input_hashes", "output_hashes"],
  "properties": {
    "schema_version": {"const": 1},
    "status": {"enum": ["passed", "failed", "error", "timeout"]},
    "returncode": {"type": ["integer", "null"]},
    "started_at": {"type": "string"},
    "duration_seconds": {"type": "number", "minimum": 0},
    "command": {"type": "array", "items": {"type": "string"}},
    "isolation": {"enum": ["local_bounded", "container"]},
    "isolation_strength": {"type": "string"},
    "stdout_path": {"type": "string"},
    "stderr_path": {"type": "string"},
    "stdout_truncated": {"type": "boolean"},
    "stderr_truncated": {"type": "boolean"},
    "input_hashes": {"type": "object", "additionalProperties": {"type": "string"}},
    "output_hashes": {"type": "object", "additionalProperties": {"type": "string"}},
    "error": {"type": ["string", "null"]}
  }
}
```

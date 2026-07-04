---
title: "Local LLM exact byte-match report"
description: "Schema reference for schemas/local-llm/report.schema.json"
---

# `schemas/local-llm/report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/local-llm/report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/local-llm/report.schema.json` |
| Title | Local LLM exact byte-match report |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 13 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

## Required fields

- `schema_version`
- `kind`
- `created_at`
- `status`
- `profile`
- `compiler_profile`
- `job`
- `attempt_limit`
- `attempt_count`
- `attempts`
- `accepted`
- `claim`
- `limitations`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `accepted` | `oneOf` | yes | — |
| `attempt_count` | `integer` | yes | — |
| `attempt_limit` | `integer` | yes | — |
| `attempts` | `array` | yes | — |
| `claim` | `string` | yes | — |
| `compiler_profile` | `object` | yes | — |
| `created_at` | `string` | yes | — |
| `job` | `object` | yes | — |
| `kind` | — | yes | — |
| `limitations` | `array` | yes | — |
| `profile` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `status` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


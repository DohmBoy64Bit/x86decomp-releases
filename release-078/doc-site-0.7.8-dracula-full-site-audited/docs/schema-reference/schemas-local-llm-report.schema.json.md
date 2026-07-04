---
title: "Local LLM exact byte-match report"
description: "Exact source-derived schema reference for schemas/local-llm/report.schema.json"
---

# `schemas/local-llm/report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/local-llm/report.schema.json` |
| SHA-256 | `d61c0308354431848f281d3c62cd32b39c9d61277492bee480a02276e5ad6ac0` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/local-llm/report.schema.json` |
| Title | Local LLM exact byte-match report |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 13 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

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
| `accepted` | `oneOf` | yes | Not declared |
| `attempt_count` | `integer` | yes | Not declared |
| `attempt_limit` | `integer` | yes | Not declared |
| `attempts` | `array` | yes | Not declared |
| `claim` | `string` | yes | Not declared |
| `compiler_profile` | `object` | yes | Not declared |
| `created_at` | `string` | yes | Not declared |
| `job` | `object` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `limitations` | `array` | yes | Not declared |
| `profile` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `status` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

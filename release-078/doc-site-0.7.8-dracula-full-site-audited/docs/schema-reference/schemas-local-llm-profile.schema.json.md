---
title: "Local LLM provider profile"
description: "Exact source-derived schema reference for schemas/local-llm/profile.schema.json"
---

# `schemas/local-llm/profile.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/local-llm/profile.schema.json` |
| SHA-256 | `dc3ed501bada8be1896567c329fd550ad843059786ed07bbae6ef3063fdfe3ee` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/local-llm/profile.schema.json` |
| Title | Local LLM provider profile |
| Top-level type | `object` |
| Top-level properties | 17 |
| Required fields | 17 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `id`
- `provider`
- `protocol`
- `base_url`
- `models_path`
- `chat_path`
- `structured_output`
- `model`
- `temperature`
- `max_tokens`
- `timeout_seconds`
- `max_response_bytes`
- `verify_tls`
- `allow_remote`
- `api_key_env`
- `headers`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `allow_remote` | `boolean` | yes | Not declared |
| `api_key_env` | `string, null` | yes | Not declared |
| `base_url` | `string` | yes | Not declared |
| `chat_path` | `string` | yes | Not declared |
| `headers` | `object` | yes | Not declared |
| `id` | `string` | yes | Not declared |
| `max_response_bytes` | `integer` | yes | Not declared |
| `max_tokens` | `integer` | yes | Not declared |
| `model` | `string` | yes | Not declared |
| `models_path` | `string` | yes | Not declared |
| `protocol` | `Not declared` | yes | Not declared |
| `provider` | `Not declared` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `structured_output` | `Not declared` | yes | Not declared |
| `temperature` | `number` | yes | Not declared |
| `timeout_seconds` | `integer` | yes | Not declared |
| `verify_tls` | `boolean` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

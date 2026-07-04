---
title: "Local LLM provider profile"
description: "Schema reference for schemas/local-llm/profile.schema.json"
---

# `schemas/local-llm/profile.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/local-llm/profile.schema.json` |
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
| `allow_remote` | `boolean` | yes | — |
| `api_key_env` | `string, null` | yes | — |
| `base_url` | `string` | yes | — |
| `chat_path` | `string` | yes | — |
| `headers` | `object` | yes | — |
| `id` | `string` | yes | — |
| `max_response_bytes` | `integer` | yes | — |
| `max_tokens` | `integer` | yes | — |
| `model` | `string` | yes | — |
| `models_path` | `string` | yes | — |
| `protocol` | — | yes | — |
| `provider` | — | yes | — |
| `schema_version` | — | yes | — |
| `structured_output` | — | yes | — |
| `temperature` | `number` | yes | — |
| `timeout_seconds` | `integer` | yes | — |
| `verify_tls` | `boolean` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


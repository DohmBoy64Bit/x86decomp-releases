---
title: "Local LLM C generation and byte-match job"
description: "Schema reference for schemas/local-llm/job.schema.json"
---

# `schemas/local-llm/job.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/local-llm/job.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/local-llm/job.schema.json` |
| Title | Local LLM C generation and byte-match job |
| Top-level type | `object` |
| Top-level properties | 16 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `id`
- `function_name`
- `architecture`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `abi` | `object` | no | — |
| `architecture` | — | yes | — |
| `base_rva` | `integer` | no | — |
| `evidence` | `object` | no | — |
| `function_name` | `string` | yes | — |
| `id` | `string` | yes | — |
| `image_base` | `integer` | no | — |
| `max_attempts` | `integer` | no | — |
| `mnemonics` | `string` | no | — |
| `mnemonics_file` | `string` | no | — |
| `schema_version` | — | yes | — |
| `section_placements` | `object` | no | — |
| `symbol` | `string` | no | — |
| `symbol_map` | `oneOf` | no | — |
| `target_bytes_file` | `string` | no | — |
| `target_bytes_hex` | `string` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


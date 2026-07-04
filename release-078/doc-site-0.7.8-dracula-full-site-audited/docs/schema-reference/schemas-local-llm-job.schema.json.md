---
title: "Local LLM C generation and byte-match job"
description: "Exact source-derived schema reference for schemas/local-llm/job.schema.json"
---

# `schemas/local-llm/job.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/local-llm/job.schema.json` |
| SHA-256 | `6ac68b5f4f22855154f8ec09e599c7caa3ce12d117fb125a0bae8e4dce0197a8` |
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
| `abi` | `object` | no | Not declared |
| `architecture` | `Not declared` | yes | Not declared |
| `base_rva` | `integer` | no | Not declared |
| `evidence` | `object` | no | Not declared |
| `function_name` | `string` | yes | Not declared |
| `id` | `string` | yes | Not declared |
| `image_base` | `integer` | no | Not declared |
| `max_attempts` | `integer` | no | Not declared |
| `mnemonics` | `string` | no | Not declared |
| `mnemonics_file` | `string` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `section_placements` | `object` | no | Not declared |
| `symbol` | `string` | no | Not declared |
| `symbol_map` | `oneOf` | no | Not declared |
| `target_bytes_file` | `string` | no | Not declared |
| `target_bytes_hex` | `string` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

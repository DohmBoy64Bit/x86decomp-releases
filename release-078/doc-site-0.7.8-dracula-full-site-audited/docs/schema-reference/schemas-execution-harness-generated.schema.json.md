---
title: "execution-harness-generated.schema.json"
description: "Exact source-derived schema reference for schemas/execution-harness-generated.schema.json"
---

# `schemas/execution-harness-generated.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/execution-harness-generated.schema.json` |
| SHA-256 | `7ba43bfcb6b5b8736d784112af5531e1a890630e379eb2c345f15442c18a2c6d` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:execution-harness-generated:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 17 |
| Required fields | 16 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

## Required fields

- `schema_version`
- `architecture`
- `code_base`
- `stack_base`
- `stack_size`
- `sentinel_address`
- `max_instructions`
- `timeout_ms`
- `registers`
- `stack_arguments_hex`
- `memory`
- `observe_registers`
- `observe_memory`
- `stubs`
- `generation`
- `limitations`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | `Not declared` | yes | Not declared |
| `code_base` | `integer` | yes | Not declared |
| `created_at` | `string` | no | Not declared |
| `generation` | `object` | yes | Not declared |
| `limitations` | `array` | yes | Not declared |
| `max_instructions` | `integer` | yes | Not declared |
| `memory` | `array` | yes | Not declared |
| `observe_memory` | `array` | yes | Not declared |
| `observe_registers` | `array` | yes | Not declared |
| `registers` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `sentinel_address` | `integer` | yes | Not declared |
| `stack_arguments_hex` | `string` | yes | Not declared |
| `stack_base` | `integer` | yes | Not declared |
| `stack_size` | `integer` | yes | Not declared |
| `stubs` | `object` | yes | Not declared |
| `timeout_ms` | `integer` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

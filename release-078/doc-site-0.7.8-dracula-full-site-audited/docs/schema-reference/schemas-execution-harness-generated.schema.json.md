---
title: "execution-harness-generated.schema.json"
description: "Schema reference for schemas/execution-harness-generated.schema.json"
---

# `schemas/execution-harness-generated.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/execution-harness-generated.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:execution-harness-generated:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 17 |
| Required fields | 16 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

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
| `architecture` | — | yes | — |
| `code_base` | `integer` | yes | — |
| `created_at` | `string` | no | — |
| `generation` | `object` | yes | — |
| `limitations` | `array` | yes | — |
| `max_instructions` | `integer` | yes | — |
| `memory` | `array` | yes | — |
| `observe_memory` | `array` | yes | — |
| `observe_registers` | `array` | yes | — |
| `registers` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `sentinel_address` | `integer` | yes | — |
| `stack_arguments_hex` | `string` | yes | — |
| `stack_base` | `integer` | yes | — |
| `stack_size` | `integer` | yes | — |
| `stubs` | `object` | yes | — |
| `timeout_ms` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


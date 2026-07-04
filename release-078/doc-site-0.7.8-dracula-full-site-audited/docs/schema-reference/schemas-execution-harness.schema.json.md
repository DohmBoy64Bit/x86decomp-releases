---
title: "Bounded Unicorn execution harness"
description: "Schema reference for schemas/execution-harness.schema.json"
---

# `schemas/execution-harness.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/execution-harness.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:execution-harness:1` |
| Title | Bounded Unicorn execution harness |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 1 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `architecture`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `code_base` | `integer` | no | — |
| `max_instructions` | `integer` | no | — |
| `memory` | `array` | no | — |
| `observe_memory` | `array` | no | — |
| `observe_registers` | `array` | no | — |
| `registers` | `object` | no | — |
| `sentinel_address` | `integer` | no | — |
| `stack_arguments_hex` | `string` | no | — |
| `stack_base` | `integer` | no | — |
| `stack_size` | `integer` | no | — |
| `stubs` | `object` | no | — |
| `timeout_ms` | `integer` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


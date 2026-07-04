---
title: "Bounded Unicorn execution harness"
description: "Exact source-derived schema reference for schemas/execution-harness.schema.json"
---

# `schemas/execution-harness.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/execution-harness.schema.json` |
| SHA-256 | `2ec27dc202dcf7ab923c646c71e30769b0c18527aaf2e6ba44e70536574e4f68` |
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
| `architecture` | `Not declared` | yes | Not declared |
| `code_base` | `integer` | no | Not declared |
| `max_instructions` | `integer` | no | Not declared |
| `memory` | `array` | no | Not declared |
| `observe_memory` | `array` | no | Not declared |
| `observe_registers` | `array` | no | Not declared |
| `registers` | `object` | no | Not declared |
| `sentinel_address` | `integer` | no | Not declared |
| `stack_arguments_hex` | `string` | no | Not declared |
| `stack_base` | `integer` | no | Not declared |
| `stack_size` | `integer` | no | Not declared |
| `stubs` | `object` | no | Not declared |
| `timeout_ms` | `integer` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

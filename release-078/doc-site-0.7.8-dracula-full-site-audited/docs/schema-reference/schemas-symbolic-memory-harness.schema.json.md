---
title: "Bounded symbolic memory and alias harness"
description: "Schema reference for schemas/symbolic-memory-harness.schema.json"
---

# `schemas/symbolic-memory-harness.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/symbolic-memory-harness.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:symbolic-memory-harness:1` |
| Title | Bounded symbolic memory and alias harness |
| Top-level type | `object` |
| Top-level properties | 11 |
| Required fields | 2 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `architecture`
- `regions`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `alias_constraints` | `array` | no | — |
| `alias_slots` | `integer` | no | — |
| `architecture` | — | yes | — |
| `input_registers` | `array` | no | — |
| `max_paths` | `integer` | no | — |
| `max_steps` | `integer` | no | — |
| `observe_memory` | `array` | no | — |
| `output_registers` | `array` | no | — |
| `regions` | `array` | yes | — |
| `slot_stride` | `integer` | no | — |
| `stack_argument_words` | `integer` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


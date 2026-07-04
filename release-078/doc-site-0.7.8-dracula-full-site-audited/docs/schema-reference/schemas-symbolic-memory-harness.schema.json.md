---
title: "Bounded symbolic memory and alias harness"
description: "Exact source-derived schema reference for schemas/symbolic-memory-harness.schema.json"
---

# `schemas/symbolic-memory-harness.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/symbolic-memory-harness.schema.json` |
| SHA-256 | `e7ce53b843c172758fc086503e040cd1c60a3836f528b2c8396a7e77ab7c200a` |
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
| `alias_constraints` | `array` | no | Not declared |
| `alias_slots` | `integer` | no | Not declared |
| `architecture` | `Not declared` | yes | Not declared |
| `input_registers` | `array` | no | Not declared |
| `max_paths` | `integer` | no | Not declared |
| `max_steps` | `integer` | no | Not declared |
| `observe_memory` | `array` | no | Not declared |
| `output_registers` | `array` | no | Not declared |
| `regions` | `array` | yes | Not declared |
| `slot_stride` | `integer` | no | Not declared |
| `stack_argument_words` | `integer` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

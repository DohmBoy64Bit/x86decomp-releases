---
title: "x86decomp function-slot"
description: "Schema reference for schemas/native/function-slot.schema.json"
---

# `schemas/native/function-slot.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/function-slot.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.invalid/schemas/native/function-slot.schema.json` |
| Title | x86decomp function-slot |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `function_id`
- `rva`
- `body_size`
- `slot_size`
- `classification`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `body_size` | `integer` | yes | — |
| `classification` | — | yes | — |
| `function_id` | `string` | yes | — |
| `rva` | `integer` | yes | — |
| `slot_size` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


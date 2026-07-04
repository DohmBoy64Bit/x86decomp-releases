---
title: "x86decomp function-match"
description: "Schema reference for schemas/native/function-match.schema.json"
---

# `schemas/native/function-match.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/function-match.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.invalid/schemas/native/function-match.schema.json` |
| Title | x86decomp function-match |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `function_id`
- `rva`
- `slot_size`
- `classification`
- `replacement_safe`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `classification` | — | yes | — |
| `function_id` | `string` | yes | — |
| `replacement_safe` | `boolean` | yes | — |
| `rva` | `integer` | yes | — |
| `slot_size` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


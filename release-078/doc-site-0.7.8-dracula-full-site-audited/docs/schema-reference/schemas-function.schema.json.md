---
title: "x86decomp Ghidra function artifact (schema versions 1 and 2)"
description: "Schema reference for schemas/function.schema.json"
---

# `schemas/function.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/function.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:function:2` |
| Title | x86decomp Ghidra function artifact (schema versions 1 and 2) |
| Top-level type | `object` |
| Top-level properties | 19 |
| Required fields | 11 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `id`
- `entry`
- `entry_rva`
- `name`
- `name_source`
- `calling_convention`
- `signature`
- `return_type`
- `body_ranges`
- `parameters`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `artifacts` | `object` | no | — |
| `body_ranges` | `array` | yes | — |
| `calling_convention` | `string, null` | yes | — |
| `decompile_completed` | `boolean` | no | — |
| `decompile_error` | `string, null` | no | — |
| `entry` | `string` | yes | — |
| `entry_rva` | `integer` | yes | — |
| `functional_status` | — | no | — |
| `id` | `string` | yes | — |
| `is_thunk` | `boolean` | no | — |
| `matching_status` | — | no | — |
| `name` | `string` | yes | — |
| `name_source` | `string` | yes | — |
| `parameters` | `array` | yes | — |
| `qualified_name` | `string` | no | — |
| `return_type` | `string` | yes | — |
| `schema_version` | — | yes | — |
| `selected_modes` | `array` | no | — |
| `signature` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


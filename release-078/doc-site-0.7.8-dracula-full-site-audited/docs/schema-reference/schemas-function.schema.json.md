---
title: "x86decomp Ghidra function artifact (schema versions 1 and 2)"
description: "Exact source-derived schema reference for schemas/function.schema.json"
---

# `schemas/function.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/function.schema.json` |
| SHA-256 | `00c65be77cc237df28a9112019c07019f88f38072ceb329907adc88bcfc34704` |
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
| `artifacts` | `object` | no | Not declared |
| `body_ranges` | `array` | yes | Not declared |
| `calling_convention` | `string, null` | yes | Not declared |
| `decompile_completed` | `boolean` | no | Not declared |
| `decompile_error` | `string, null` | no | Not declared |
| `entry` | `string` | yes | Not declared |
| `entry_rva` | `integer` | yes | Not declared |
| `functional_status` | `Not declared` | no | Not declared |
| `id` | `string` | yes | Not declared |
| `is_thunk` | `boolean` | no | Not declared |
| `matching_status` | `Not declared` | no | Not declared |
| `name` | `string` | yes | Not declared |
| `name_source` | `string` | yes | Not declared |
| `parameters` | `array` | yes | Not declared |
| `qualified_name` | `string` | no | Not declared |
| `return_type` | `string` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `selected_modes` | `array` | no | Not declared |
| `signature` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

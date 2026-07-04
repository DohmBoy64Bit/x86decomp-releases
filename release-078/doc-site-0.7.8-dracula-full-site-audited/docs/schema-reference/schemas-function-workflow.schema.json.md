---
title: "x86decomp per-function workflow"
description: "Schema reference for schemas/function-workflow.schema.json"
---

# `schemas/function-workflow.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/function-workflow.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:function-workflow:2` |
| Title | x86decomp per-function workflow |
| Top-level type | `object` |
| Top-level properties | 11 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `function_id`
- `selected_modes`
- `source_stage`
- `matching_status`
- `functional_status`
- `reports`
- `blockers`
- `updated_at`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `active_candidate` | `string, null` | no | — |
| `blockers` | `array` | yes | — |
| `compiler_profile` | `string, null` | no | — |
| `function_id` | `string` | yes | — |
| `functional_status` | — | yes | — |
| `matching_status` | — | yes | — |
| `reports` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `selected_modes` | `array` | yes | — |
| `source_stage` | — | yes | — |
| `updated_at` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


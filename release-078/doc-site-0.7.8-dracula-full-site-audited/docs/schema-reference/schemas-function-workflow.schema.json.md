---
title: "x86decomp per-function workflow"
description: "Exact source-derived schema reference for schemas/function-workflow.schema.json"
---

# `schemas/function-workflow.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/function-workflow.schema.json` |
| SHA-256 | `972f7c4fef555a4653a57cad04f1dedb186cc70a6c59de7e674645b30c240351` |
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
| `active_candidate` | `string, null` | no | Not declared |
| `blockers` | `array` | yes | Not declared |
| `compiler_profile` | `string, null` | no | Not declared |
| `function_id` | `string` | yes | Not declared |
| `functional_status` | `Not declared` | yes | Not declared |
| `matching_status` | `Not declared` | yes | Not declared |
| `reports` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `selected_modes` | `array` | yes | Not declared |
| `source_stage` | `Not declared` | yes | Not declared |
| `updated_at` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

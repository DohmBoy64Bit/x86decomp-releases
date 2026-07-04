---
title: "Validator-gated work item"
description: "Exact source-derived schema reference for schemas/work-task.schema.json"
---

# `schemas/work-task.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/work-task.schema.json` |
| SHA-256 | `36794b2e24e785918a28d8bd7f5fedd100c090ed64030c71eefa0a8c933b92c9` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:work-task:1` |
| Title | Validator-gated work item |
| Top-level type | `object` |
| Top-level properties | 14 |
| Required fields | 12 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `id`
- `function_id`
- `mode`
- `kind`
- `status`
- `priority`
- `instructions`
- `required_validators`
- `validator_results`
- `evidence_ids`
- `created_at`
- `updated_at`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `assignee` | `string, null` | no | Not declared |
| `created_at` | `string` | yes | Not declared |
| `evidence_ids` | `array` | yes | Not declared |
| `function_id` | `string` | yes | Not declared |
| `id` | `string` | yes | Not declared |
| `instructions` | `string` | yes | Not declared |
| `kind` | `string` | yes | Not declared |
| `mode` | `Not declared` | yes | Not declared |
| `priority` | `integer` | yes | Not declared |
| `proposal` | `object, null` | no | Not declared |
| `required_validators` | `array` | yes | Not declared |
| `status` | `Not declared` | yes | Not declared |
| `updated_at` | `string` | yes | Not declared |
| `validator_results` | `object` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

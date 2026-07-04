---
title: "Validator-gated work item"
description: "Schema reference for schemas/work-task.schema.json"
---

# `schemas/work-task.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/work-task.schema.json` |
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
| `assignee` | `string, null` | no | — |
| `created_at` | `string` | yes | — |
| `evidence_ids` | `array` | yes | — |
| `function_id` | `string` | yes | — |
| `id` | `string` | yes | — |
| `instructions` | `string` | yes | — |
| `kind` | `string` | yes | — |
| `mode` | — | yes | — |
| `priority` | `integer` | yes | — |
| `proposal` | `object, null` | no | — |
| `required_validators` | `array` | yes | — |
| `status` | — | yes | — |
| `updated_at` | `string` | yes | — |
| `validator_results` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


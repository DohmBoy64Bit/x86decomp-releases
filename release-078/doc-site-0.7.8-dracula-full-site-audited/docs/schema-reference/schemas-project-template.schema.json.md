---
title: "Grounded x86decomp project-template contract"
description: "Schema reference for schemas/project-template.schema.json"
---

# `schemas/project-template.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/project-template.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:project-template:1` |
| Title | Grounded x86decomp project-template contract |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 11 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `created_at`
- `target_id`
- `architecture`
- `image_kind`
- `selected_modes`
- `matching`
- `functional`
- `artifact_roles`
- `blockers`
- `truth_policy`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `artifact_roles` | `array` | yes | — |
| `blockers` | `array` | yes | — |
| `created_at` | `string` | yes | — |
| `functional` | `object` | yes | — |
| `image_kind` | — | yes | — |
| `matching` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `selected_modes` | `array` | yes | — |
| `source_language_candidates` | `array` | no | — |
| `source_language_decision` | `string` | no | — |
| `target_id` | `string` | yes | — |
| `truth_policy` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


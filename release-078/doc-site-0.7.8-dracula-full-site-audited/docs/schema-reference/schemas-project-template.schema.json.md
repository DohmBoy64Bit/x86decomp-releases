---
title: "Grounded x86decomp project-template contract"
description: "Exact source-derived schema reference for schemas/project-template.schema.json"
---

# `schemas/project-template.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/project-template.schema.json` |
| SHA-256 | `1bf881ea328d3a6c00d727c0cbe1e47763726e70362a085354178add994458ce` |
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
| `architecture` | `Not declared` | yes | Not declared |
| `artifact_roles` | `array` | yes | Not declared |
| `blockers` | `array` | yes | Not declared |
| `created_at` | `string` | yes | Not declared |
| `functional` | `object` | yes | Not declared |
| `image_kind` | `Not declared` | yes | Not declared |
| `matching` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `selected_modes` | `array` | yes | Not declared |
| `source_language_candidates` | `array` | no | Not declared |
| `source_language_decision` | `string` | no | Not declared |
| `target_id` | `string` | yes | Not declared |
| `truth_policy` | `object` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

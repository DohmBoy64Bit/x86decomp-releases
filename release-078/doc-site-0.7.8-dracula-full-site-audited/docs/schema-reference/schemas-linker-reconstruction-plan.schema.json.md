---
title: "linker-reconstruction-plan.schema.json"
description: "Exact source-derived schema reference for schemas/linker-reconstruction-plan.schema.json"
---

# `schemas/linker-reconstruction-plan.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/linker-reconstruction-plan.schema.json` |
| SHA-256 | `1d6fadf9737abed4d02cc90d3859898785edf62d3909c39fe893c8841c57f504` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:linker-reconstruction-plan:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 17 |
| Required fields | 11 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

## Required fields

- `schema_version`
- `kind`
- `reference_image`
- `map`
- `objects`
- `sections`
- `placements`
- `comdat_resolution`
- `relink_manifest`
- `unresolved`
- `ready_for_relink`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `archives` | `array` | no | Not declared |
| `comdat_resolution` | `object` | yes | Not declared |
| `complete_original_link_command_claimed` | `Not declared` | no | Not declared |
| `created_at` | `string` | no | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `libraries` | `array` | no | Not declared |
| `limitations` | `array` | no | Not declared |
| `linker` | `string` | no | Not declared |
| `map` | `object` | yes | Not declared |
| `objects` | `array` | yes | Not declared |
| `placements` | `array` | yes | Not declared |
| `ready_for_relink` | `boolean` | yes | Not declared |
| `reference_image` | `object` | yes | Not declared |
| `relink_manifest` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `sections` | `array` | yes | Not declared |
| `unresolved` | `array` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

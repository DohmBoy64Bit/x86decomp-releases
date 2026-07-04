---
title: "linker-reconstruction-plan.schema.json"
description: "Schema reference for schemas/linker-reconstruction-plan.schema.json"
---

# `schemas/linker-reconstruction-plan.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/linker-reconstruction-plan.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:linker-reconstruction-plan:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 17 |
| Required fields | 11 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

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
| `archives` | `array` | no | — |
| `comdat_resolution` | `object` | yes | — |
| `complete_original_link_command_claimed` | — | no | — |
| `created_at` | `string` | no | — |
| `kind` | — | yes | — |
| `libraries` | `array` | no | — |
| `limitations` | `array` | no | — |
| `linker` | `string` | no | — |
| `map` | `object` | yes | — |
| `objects` | `array` | yes | — |
| `placements` | `array` | yes | — |
| `ready_for_relink` | `boolean` | yes | — |
| `reference_image` | `object` | yes | — |
| `relink_manifest` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `sections` | `array` | yes | — |
| `unresolved` | `array` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


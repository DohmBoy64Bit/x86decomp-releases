---
title: "Linker layout reconstruction report"
description: "Schema reference for schemas/linker-layout.schema.json"
---

# `schemas/linker-layout.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/linker-layout.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:linker-layout:1` |
| Title | Linker layout reconstruction report |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `image`
- `map`
- `contributions`
- `unresolved`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `comdat_resolution` | `object, null` | no | — |
| `complete_original_layout_claimed` | `boolean` | no | — |
| `contributions` | `array` | yes | — |
| `image` | `object` | yes | — |
| `kind` | — | yes | — |
| `map` | `object` | yes | — |
| `object_order_evidenced` | `boolean` | no | — |
| `schema_version` | — | yes | — |
| `unresolved` | `array` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


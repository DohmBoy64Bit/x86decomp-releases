---
title: "Linker layout reconstruction report"
description: "Exact source-derived schema reference for schemas/linker-layout.schema.json"
---

# `schemas/linker-layout.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/linker-layout.schema.json` |
| SHA-256 | `a8faf6022c8b70e04c3375d47a480b9a811e72edd55ea7e0ec4e80a77a8ca934` |
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
| `comdat_resolution` | `object, null` | no | Not declared |
| `complete_original_layout_claimed` | `boolean` | no | Not declared |
| `contributions` | `array` | yes | Not declared |
| `image` | `object` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `map` | `object` | yes | Not declared |
| `object_order_evidenced` | `boolean` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `unresolved` | `array` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

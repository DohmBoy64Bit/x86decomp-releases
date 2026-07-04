---
title: "cpp-recovery.schema.json"
description: "Schema reference for schemas/cpp-recovery.schema.json"
---

# `schemas/cpp-recovery.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/cpp-recovery.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:cpp-recovery:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

## Required fields

- `schema_version`
- `kind`
- `classes`
- `vtable_groups`
- `adjustor_thunk_candidates`
- `counts`
- `claims`
- `limitations`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `adjustor_thunk_candidates` | `array` | yes | — |
| `claims` | `object` | yes | — |
| `classes` | `array` | yes | — |
| `counts` | `object` | yes | — |
| `created_at` | `string` | no | — |
| `image` | `object, null` | no | — |
| `kind` | — | yes | — |
| `limitations` | `array` | yes | — |
| `metadata_source` | `string` | no | — |
| `schema_version` | — | yes | — |
| `static_initializer_order_evidence` | `array` | no | — |
| `vtable_groups` | `array` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


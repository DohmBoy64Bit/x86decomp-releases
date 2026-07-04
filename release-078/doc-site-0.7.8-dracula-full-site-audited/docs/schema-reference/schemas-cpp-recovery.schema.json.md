---
title: "cpp-recovery.schema.json"
description: "Exact source-derived schema reference for schemas/cpp-recovery.schema.json"
---

# `schemas/cpp-recovery.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/cpp-recovery.schema.json` |
| SHA-256 | `9eda5eb04cdd6404ed82077dab0b1f2668f3682b33f864fec3c7348439515d8a` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:cpp-recovery:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

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
| `adjustor_thunk_candidates` | `array` | yes | Not declared |
| `claims` | `object` | yes | Not declared |
| `classes` | `array` | yes | Not declared |
| `counts` | `object` | yes | Not declared |
| `created_at` | `string` | no | Not declared |
| `image` | `object, null` | no | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `limitations` | `array` | yes | Not declared |
| `metadata_source` | `string` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `static_initializer_order_evidence` | `array` | no | Not declared |
| `vtable_groups` | `array` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

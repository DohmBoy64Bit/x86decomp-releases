---
title: "review item"
description: "Exact source-derived schema reference for schemas/governance/review.schema.json"
---

# `schemas/governance/review.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/review.schema.json` |
| SHA-256 | `280cfe7963adcdcbbb3a1fde01b921cad82751d2240a4fcdaa9b9543db071bc2` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `Not declared` |
| Title | review item |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `kind`
- `subject_id`
- `priority`
- `status`
- `summary`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `details` | `object` | no | Not declared |
| `kind` | `string` | yes | Not declared |
| `locked` | `boolean` | no | Not declared |
| `priority` | `integer` | yes | Not declared |
| `status` | `Not declared` | yes | Not declared |
| `subject_id` | `string` | yes | Not declared |
| `summary` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

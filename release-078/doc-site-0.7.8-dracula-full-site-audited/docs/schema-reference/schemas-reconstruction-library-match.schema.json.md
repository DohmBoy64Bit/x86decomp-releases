---
title: "Static library recognition candidate"
description: "Schema reference for schemas/reconstruction/library-match.schema.json"
---

# `schemas/reconstruction/library-match.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/library-match.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/library-match.schema.json` |
| Title | Static library recognition candidate |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `match_id`
- `subject_id`
- `library_name`
- `confidence`
- `evidence`
- `disposition`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `confidence` | `number` | yes | — |
| `disposition` | — | yes | — |
| `evidence` | `array` | yes | — |
| `library_name` | `string` | yes | — |
| `match_id` | `string` | yes | — |
| `subject_id` | `string` | yes | — |
| `version_range` | `string, null` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


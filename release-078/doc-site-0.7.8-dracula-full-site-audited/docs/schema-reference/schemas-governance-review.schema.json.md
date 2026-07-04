---
title: "review item"
description: "Schema reference for schemas/governance/review.schema.json"
---

# `schemas/governance/review.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/review.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | — |
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
| `details` | `object` | no | — |
| `kind` | `string` | yes | — |
| `locked` | `boolean` | no | — |
| `priority` | `integer` | yes | — |
| `status` | — | yes | — |
| `subject_id` | `string` | yes | — |
| `summary` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


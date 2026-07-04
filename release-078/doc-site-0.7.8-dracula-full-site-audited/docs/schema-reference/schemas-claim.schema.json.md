---
title: "x86decomp claim"
description: "Schema reference for schemas/claim.schema.json"
---

# `schemas/claim.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/claim.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:claim:1` |
| Title | x86decomp claim |
| Top-level type | `object` |
| Top-level properties | 10 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

## Required fields

- `id`
- `subject`
- `predicate`
- `object`
- `state`
- `evidence_ids`
- `contradiction_ids`
- `notes`
- `created_at`
- `updated_at`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `contradiction_ids` | `array` | yes | — |
| `created_at` | `string` | yes | — |
| `evidence_ids` | `array` | yes | — |
| `id` | `string` | yes | — |
| `notes` | `array` | yes | — |
| `object` | `string` | yes | — |
| `predicate` | `string` | yes | — |
| `state` | — | yes | — |
| `subject` | `string` | yes | — |
| `updated_at` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


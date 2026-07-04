---
title: "x86decomp patch-plan"
description: "Schema reference for schemas/native/patch-plan.schema.json"
---

# `schemas/native/patch-plan.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/patch-plan.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.invalid/schemas/native/patch-plan.schema.json` |
| Title | x86decomp patch-plan |
| Top-level type | `object` |
| Top-level properties | 3 |
| Required fields | 3 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `original_path`
- `output_path`
- `operations`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `operations` | `array` | yes | — |
| `original_path` | `string` | yes | — |
| `output_path` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


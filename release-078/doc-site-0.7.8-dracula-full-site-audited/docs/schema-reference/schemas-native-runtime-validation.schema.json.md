---
title: "x86decomp runtime-validation"
description: "Schema reference for schemas/native/runtime-validation.schema.json"
---

# `schemas/native/runtime-validation.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/runtime-validation.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.invalid/schemas/native/runtime-validation.schema.json` |
| Title | x86decomp runtime-validation |
| Top-level type | `object` |
| Top-level properties | 4 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `image_path`
- `validation_kind`
- `status`
- `checks`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `checks` | `object` | yes | — |
| `image_path` | `string` | yes | — |
| `status` | — | yes | — |
| `validation_kind` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


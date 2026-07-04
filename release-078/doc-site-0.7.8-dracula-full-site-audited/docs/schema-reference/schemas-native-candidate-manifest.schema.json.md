---
title: "x86decomp candidate-manifest"
description: "Schema reference for schemas/native/candidate-manifest.schema.json"
---

# `schemas/native/candidate-manifest.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/candidate-manifest.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.invalid/schemas/native/candidate-manifest.schema.json` |
| Title | x86decomp candidate-manifest |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `function_id`
- `rva`
- `slot_size`
- `candidate_path`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate_path` | `string` | yes | — |
| `function_id` | `string` | yes | — |
| `rva` | `oneOf` | yes | — |
| `slot_size` | `integer` | yes | — |
| `symbol` | `string, null` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


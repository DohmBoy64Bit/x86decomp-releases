---
title: "Compiler experiment matrix"
description: "Schema reference for schemas/compiler-lab.schema.json"
---

# `schemas/compiler-lab.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/compiler-lab.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:compiler-lab:1` |
| Title | Compiler experiment matrix |
| Top-level type | `object` |
| Top-level properties | 8 |
| Required fields | 2 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `source`
- `profiles`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `cache_root` | `string` | no | — |
| `matrix` | `object` | no | — |
| `max_experiments` | `integer` | no | — |
| `output_name` | `string` | no | — |
| `output_root` | `string` | no | — |
| `profiles` | `array` | yes | — |
| `source` | `string` | yes | — |
| `target` | `oneOf` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


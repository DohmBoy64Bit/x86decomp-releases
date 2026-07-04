---
title: "v0.7.8 COFF relocation resolution"
description: "Schema reference for schemas/assembly/relocation-resolution.schema.json"
---

# `schemas/assembly/relocation-resolution.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/assembly/relocation-resolution.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/assembly/relocation-resolution.schema.json` |
| Title | v0.7.8 COFF relocation resolution |
| Top-level type | `object` |
| Top-level properties | 8 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `object`
- `symbol`
- `architecture`
- `base_rva`
- `resolved_count`
- `unresolved_count`
- `relocations`
- `exact_match`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `base_rva` | `integer` | yes | — |
| `exact_match` | `boolean` | yes | — |
| `object` | `string` | yes | — |
| `relocations` | `array` | yes | — |
| `resolved_count` | `integer` | yes | — |
| `symbol` | `string` | yes | — |
| `unresolved_count` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


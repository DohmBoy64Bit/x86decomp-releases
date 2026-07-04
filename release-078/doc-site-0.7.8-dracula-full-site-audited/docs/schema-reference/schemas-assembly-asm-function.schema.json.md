---
title: "v0.7.8 function assembly result"
description: "Schema reference for schemas/assembly/asm-function.schema.json"
---

# `schemas/assembly/asm-function.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/assembly/asm-function.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/assembly/asm-function.schema.json` |
| Title | v0.7.8 function assembly result |
| Top-level type | `object` |
| Top-level properties | 14 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `function_id`
- `symbol`
- `rva`
- `format`
- `classification`
- `exact_match`
- `input_sha256`
- `source_sha256`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `byte_escape_count` | `integer` | no | — |
| `classification` | — | yes | — |
| `exact_match` | `boolean` | yes | — |
| `format` | — | yes | — |
| `function_id` | `string` | yes | — |
| `input_sha256` | `string` | yes | — |
| `instruction_count` | `integer` | no | — |
| `mnemonic_count` | `integer` | no | — |
| `relocation_count` | `integer` | no | — |
| `resolved_relocation_count` | `integer` | no | — |
| `rva` | `integer` | yes | — |
| `source_sha256` | `string` | yes | — |
| `symbol` | `string` | yes | — |
| `unresolved_relocation_count` | `integer` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


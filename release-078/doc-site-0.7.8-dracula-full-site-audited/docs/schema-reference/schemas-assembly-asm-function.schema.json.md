---
title: "v0.7.8 function assembly result"
description: "Exact source-derived schema reference for schemas/assembly/asm-function.schema.json"
---

# `schemas/assembly/asm-function.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/assembly/asm-function.schema.json` |
| SHA-256 | `db7f1658e6121216219cbe02f674ad829a1dc71fd1e38ff60be82909aeff852f` |
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
| `byte_escape_count` | `integer` | no | Not declared |
| `classification` | `Not declared` | yes | Not declared |
| `exact_match` | `boolean` | yes | Not declared |
| `format` | `Not declared` | yes | Not declared |
| `function_id` | `string` | yes | Not declared |
| `input_sha256` | `string` | yes | Not declared |
| `instruction_count` | `integer` | no | Not declared |
| `mnemonic_count` | `integer` | no | Not declared |
| `relocation_count` | `integer` | no | Not declared |
| `resolved_relocation_count` | `integer` | no | Not declared |
| `rva` | `integer` | yes | Not declared |
| `source_sha256` | `string` | yes | Not declared |
| `symbol` | `string` | yes | Not declared |
| `unresolved_relocation_count` | `integer` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

---
title: "v0.7.8 COFF relocation resolution"
description: "Exact source-derived schema reference for schemas/assembly/relocation-resolution.schema.json"
---

# `schemas/assembly/relocation-resolution.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/assembly/relocation-resolution.schema.json` |
| SHA-256 | `12f0d874e789ea1fb40eed10321b5b24d6e9231630c0b24bb2c39fe843e192cf` |
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
| `architecture` | `Not declared` | yes | Not declared |
| `base_rva` | `integer` | yes | Not declared |
| `exact_match` | `boolean` | yes | Not declared |
| `object` | `string` | yes | Not declared |
| `relocations` | `array` | yes | Not declared |
| `resolved_count` | `integer` | yes | Not declared |
| `symbol` | `string` | yes | Not declared |
| `unresolved_count` | `integer` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

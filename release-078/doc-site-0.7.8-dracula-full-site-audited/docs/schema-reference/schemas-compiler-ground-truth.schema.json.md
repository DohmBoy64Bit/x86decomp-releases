---
title: "Compiler ground-truth corpus manifest"
description: "Schema reference for schemas/compiler-ground-truth.schema.json"
---

# `schemas/compiler-ground-truth.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/compiler-ground-truth.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:compiler-ground-truth:1` |
| Title | Compiler ground-truth corpus manifest |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 3 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `compilers`
- `cases`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `cases` | `array` | yes | — |
| `compilers` | `array` | yes | — |
| `flag_matrix` | `object` | no | — |
| `schema_version` | — | yes | — |
| `timeout_seconds` | `integer` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


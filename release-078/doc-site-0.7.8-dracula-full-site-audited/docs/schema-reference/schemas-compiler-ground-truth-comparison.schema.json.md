---
title: "Compiler/version ground-truth corpus comparison"
description: "Schema reference for schemas/compiler-ground-truth-comparison.schema.json"
---

# `schemas/compiler-ground-truth-comparison.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/compiler-ground-truth-comparison.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:compiler-ground-truth-comparison:1` |
| Title | Compiler/version ground-truth corpus comparison |
| Top-level type | `object` |
| Top-level properties | 6 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `reports`
- `comparisons`
- `summary`
- `semantic_equivalence_claimed`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `comparisons` | `array` | yes | — |
| `kind` | — | yes | — |
| `reports` | `array` | yes | — |
| `schema_version` | — | yes | — |
| `semantic_equivalence_claimed` | — | yes | — |
| `summary` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


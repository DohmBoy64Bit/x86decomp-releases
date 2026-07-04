---
title: "PE function to COFF symbol comparison"
description: "Schema reference for schemas/exe-diff-report.schema.json"
---

# `schemas/exe-diff-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/exe-diff-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:exe-diff-report:2` |
| Title | PE function to COFF symbol comparison |
| Top-level type | `object` |
| Top-level properties | 14 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `classification`
- `pe`
- `coff`
- `normalization_masks`
- `raw_byte_comparison`
- `normalized_byte_comparison`
- `semantic_equivalence_claimed`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | no | — |
| `classification` | — | yes | — |
| `coff` | `object` | yes | — |
| `created_at` | `string` | no | — |
| `instruction_comparison` | `object, null` | no | — |
| `instruction_comparison_error` | `string, null` | no | — |
| `kind` | — | no | — |
| `limitations` | `array` | no | — |
| `normalization_masks` | `array` | yes | — |
| `normalized_byte_comparison` | `object` | yes | — |
| `pe` | `object` | yes | — |
| `raw_byte_comparison` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `semantic_equivalence_claimed` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


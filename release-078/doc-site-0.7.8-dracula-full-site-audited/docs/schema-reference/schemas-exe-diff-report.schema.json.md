---
title: "PE function to COFF symbol comparison"
description: "Exact source-derived schema reference for schemas/exe-diff-report.schema.json"
---

# `schemas/exe-diff-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/exe-diff-report.schema.json` |
| SHA-256 | `3bfb70b7158750523074f638ff5955cc519097a37543f9f097909f4576373b50` |
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
| `architecture` | `Not declared` | no | Not declared |
| `classification` | `Not declared` | yes | Not declared |
| `coff` | `object` | yes | Not declared |
| `created_at` | `string` | no | Not declared |
| `instruction_comparison` | `object, null` | no | Not declared |
| `instruction_comparison_error` | `string, null` | no | Not declared |
| `kind` | `Not declared` | no | Not declared |
| `limitations` | `array` | no | Not declared |
| `normalization_masks` | `array` | yes | Not declared |
| `normalized_byte_comparison` | `object` | yes | Not declared |
| `pe` | `object` | yes | Not declared |
| `raw_byte_comparison` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `semantic_equivalence_claimed` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

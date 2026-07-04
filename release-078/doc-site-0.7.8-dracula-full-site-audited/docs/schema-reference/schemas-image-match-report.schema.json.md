---
title: "Target-specific whole-image match report"
description: "Schema reference for schemas/image-match-report.schema.json"
---

# `schemas/image-match-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/image-match-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:image-match-report:1` |
| Title | Target-specific whole-image match report |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `reference`
- `candidate`
- `profile`
- `raw_exact_match`
- `normalized_match`
- `sections`
- `classification`
- `universal_equivalence_claimed`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate` | `object` | yes | — |
| `classification` | — | yes | — |
| `kind` | — | yes | — |
| `normalized_match` | `boolean` | yes | — |
| `normalized_mismatch_count` | `integer` | no | — |
| `profile` | `object` | yes | — |
| `raw_exact_match` | `boolean` | yes | — |
| `raw_mismatch_count` | `integer` | no | — |
| `reference` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `sections` | `array` | yes | — |
| `universal_equivalence_claimed` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


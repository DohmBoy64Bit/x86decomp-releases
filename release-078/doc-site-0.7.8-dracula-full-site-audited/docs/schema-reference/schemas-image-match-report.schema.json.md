---
title: "Target-specific whole-image match report"
description: "Exact source-derived schema reference for schemas/image-match-report.schema.json"
---

# `schemas/image-match-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/image-match-report.schema.json` |
| SHA-256 | `f81f81c2581b2941b9a3850aa2d296957e1d14de2ad3d8ee92839b34ccfadc23` |
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
| `candidate` | `object` | yes | Not declared |
| `classification` | `Not declared` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `normalized_match` | `boolean` | yes | Not declared |
| `normalized_mismatch_count` | `integer` | no | Not declared |
| `profile` | `object` | yes | Not declared |
| `raw_exact_match` | `boolean` | yes | Not declared |
| `raw_mismatch_count` | `integer` | no | Not declared |
| `reference` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `sections` | `array` | yes | Not declared |
| `universal_equivalence_claimed` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

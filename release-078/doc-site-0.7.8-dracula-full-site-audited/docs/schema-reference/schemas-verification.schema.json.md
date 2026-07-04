---
title: "x86decomp byte verification report"
description: "Schema reference for schemas/verification.schema.json"
---

# `schemas/verification.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/verification.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:verification:1` |
| Title | x86decomp byte verification report |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 13 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

## Required fields

- `schema_version`
- `created_at`
- `equal`
- `target_size`
- `candidate_size`
- `target_sha256`
- `candidate_sha256`
- `matching_prefix_bytes`
- `matching_suffix_bytes`
- `sequence_similarity`
- `reported_mismatches`
- `mismatch_report_truncated`
- `semantic_equivalence_claimed`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate_sha256` | `string` | yes | — |
| `candidate_size` | `integer` | yes | — |
| `created_at` | `string` | yes | — |
| `equal` | `boolean` | yes | — |
| `matching_prefix_bytes` | `integer` | yes | — |
| `matching_suffix_bytes` | `integer` | yes | — |
| `mismatch_report_truncated` | `boolean` | yes | — |
| `reported_mismatches` | `array` | yes | — |
| `schema_version` | — | yes | — |
| `semantic_equivalence_claimed` | — | yes | — |
| `sequence_similarity` | `number` | yes | — |
| `target_sha256` | `string` | yes | — |
| `target_size` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


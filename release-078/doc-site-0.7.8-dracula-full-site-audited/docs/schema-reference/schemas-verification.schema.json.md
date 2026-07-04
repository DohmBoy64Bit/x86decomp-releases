---
title: "x86decomp byte verification report"
description: "Exact source-derived schema reference for schemas/verification.schema.json"
---

# `schemas/verification.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/verification.schema.json` |
| SHA-256 | `a70e3422e6b0bec967695257c7b66d44f17a0cfe3f15d99799eb1c038ccb7fa0` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:verification:1` |
| Title | x86decomp byte verification report |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 13 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

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
| `candidate_sha256` | `string` | yes | Not declared |
| `candidate_size` | `integer` | yes | Not declared |
| `created_at` | `string` | yes | Not declared |
| `equal` | `boolean` | yes | Not declared |
| `matching_prefix_bytes` | `integer` | yes | Not declared |
| `matching_suffix_bytes` | `integer` | yes | Not declared |
| `mismatch_report_truncated` | `boolean` | yes | Not declared |
| `reported_mismatches` | `array` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `semantic_equivalence_claimed` | `Not declared` | yes | Not declared |
| `sequence_similarity` | `number` | yes | Not declared |
| `target_sha256` | `string` | yes | Not declared |
| `target_size` | `integer` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

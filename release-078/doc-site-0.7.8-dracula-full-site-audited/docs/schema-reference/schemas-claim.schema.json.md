---
title: "x86decomp claim"
description: "Exact source-derived schema reference for schemas/claim.schema.json"
---

# `schemas/claim.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/claim.schema.json` |
| SHA-256 | `362341adcb81640a7839c77d37d7203b911e7e79655be6c0ab4115f460609532` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:claim:1` |
| Title | x86decomp claim |
| Top-level type | `object` |
| Top-level properties | 10 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

## Required fields

- `id`
- `subject`
- `predicate`
- `object`
- `state`
- `evidence_ids`
- `contradiction_ids`
- `notes`
- `created_at`
- `updated_at`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `contradiction_ids` | `array` | yes | Not declared |
| `created_at` | `string` | yes | Not declared |
| `evidence_ids` | `array` | yes | Not declared |
| `id` | `string` | yes | Not declared |
| `notes` | `array` | yes | Not declared |
| `object` | `string` | yes | Not declared |
| `predicate` | `string` | yes | Not declared |
| `state` | `Not declared` | yes | Not declared |
| `subject` | `string` | yes | Not declared |
| `updated_at` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

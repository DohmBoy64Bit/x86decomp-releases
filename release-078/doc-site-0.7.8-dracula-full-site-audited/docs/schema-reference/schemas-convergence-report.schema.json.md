---
title: "convergence-report.schema.json"
description: "Exact source-derived schema reference for schemas/convergence-report.schema.json"
---

# `schemas/convergence-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/convergence-report.schema.json` |
| SHA-256 | `ace195921a16f72366e2920e6e2ce4e464b51f665d4d12ff5117dbea49119185` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:convergence-report:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 14 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

## Required fields

- `schema_version`
- `kind`
- `reference_sha256`
- `candidate_sha256`
- `image_match`
- `totals`
- `sections`
- `next_actions`
- `complete`
- `normalized_complete`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate_sha256` | `string` | yes | Not declared |
| `complete` | `boolean` | yes | Not declared |
| `created_at` | `string` | no | Not declared |
| `delta_from_previous` | `object, null` | no | Not declared |
| `image_match` | `object` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `limitations` | `array` | no | Not declared |
| `next_actions` | `array` | yes | Not declared |
| `normalized_complete` | `boolean` | yes | Not declared |
| `reference_sha256` | `string` | yes | Not declared |
| `root_cause_claimed` | `Not declared` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `sections` | `array` | yes | Not declared |
| `totals` | `object` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

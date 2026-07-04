---
title: "convergence-report.schema.json"
description: "Schema reference for schemas/convergence-report.schema.json"
---

# `schemas/convergence-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/convergence-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:convergence-report:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 14 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

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
| `candidate_sha256` | `string` | yes | — |
| `complete` | `boolean` | yes | — |
| `created_at` | `string` | no | — |
| `delta_from_previous` | `object, null` | no | — |
| `image_match` | `object` | yes | — |
| `kind` | — | yes | — |
| `limitations` | `array` | no | — |
| `next_actions` | `array` | yes | — |
| `normalized_complete` | `boolean` | yes | — |
| `reference_sha256` | `string` | yes | — |
| `root_cause_claimed` | — | no | — |
| `schema_version` | — | yes | — |
| `sections` | `array` | yes | — |
| `totals` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


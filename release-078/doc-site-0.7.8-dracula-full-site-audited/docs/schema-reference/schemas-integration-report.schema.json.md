---
title: "Bounded integration comparison report"
description: "Exact source-derived schema reference for schemas/integration-report.schema.json"
---

# `schemas/integration-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/integration-report.schema.json` |
| SHA-256 | `4732a3a8f4038739f46c7b7b74b20999c68d9f637bac783a53b03eee91e91d1a` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:integration-report:1` |
| Title | Bounded integration comparison report |
| Top-level type | `object` |
| Top-level properties | 8 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `created_at`
- `kind`
- `execution`
- `scenario_count`
- `passed_count`
- `failed_count`
- `all_scenarios_equivalent`
- `scenarios`
- `limitations`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `all_scenarios_equivalent` | `boolean` | yes | Not declared |
| `failed_count` | `integer` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `limitations` | `array` | yes | Not declared |
| `passed_count` | `integer` | yes | Not declared |
| `scenario_count` | `integer` | yes | Not declared |
| `scenarios` | `array` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

---
title: "Bounded integration comparison report"
description: "Schema reference for schemas/integration-report.schema.json"
---

# `schemas/integration-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/integration-report.schema.json` |
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
| `all_scenarios_equivalent` | `boolean` | yes | — |
| `failed_count` | `integer` | yes | — |
| `kind` | — | yes | — |
| `limitations` | `array` | yes | — |
| `passed_count` | `integer` | yes | — |
| `scenario_count` | `integer` | yes | — |
| `scenarios` | `array` | yes | — |
| `schema_version` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "x86decomp Static Test Bundle Report"
description: "Schema reference for schemas/test-bundle-report.schema.json"
---

# `schemas/test-bundle-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/test-bundle-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:test-bundle-report:1` |
| Title | x86decomp Static Test Bundle Report |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

## Required fields

- `schema_version`
- `kind`
- `archive`
- `bundle`
- `artifacts`
- `analyses`
- `errors`
- `static_analysis_only`
- `supplied_code_executed`
- `passed`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `analyses` | `object` | yes | — |
| `archive` | `object` | yes | — |
| `artifacts` | `array` | yes | — |
| `bundle` | `object` | yes | — |
| `created_at` | `string` | no | — |
| `errors` | `array` | yes | — |
| `kind` | — | yes | — |
| `limitations` | `array` | no | — |
| `passed` | `boolean` | yes | — |
| `schema_version` | — | yes | — |
| `static_analysis_only` | — | yes | — |
| `supplied_code_executed` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


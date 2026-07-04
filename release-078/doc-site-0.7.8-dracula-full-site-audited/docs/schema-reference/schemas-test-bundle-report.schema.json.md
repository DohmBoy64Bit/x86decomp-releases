---
title: "x86decomp Static Test Bundle Report"
description: "Exact source-derived schema reference for schemas/test-bundle-report.schema.json"
---

# `schemas/test-bundle-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/test-bundle-report.schema.json` |
| SHA-256 | `482f5b618cd46eb5e815392f2655bb9fe4f3683e1f5122b8f7ab0ea69f8a2820` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:test-bundle-report:1` |
| Title | x86decomp Static Test Bundle Report |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

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
| `analyses` | `object` | yes | Not declared |
| `archive` | `object` | yes | Not declared |
| `artifacts` | `array` | yes | Not declared |
| `bundle` | `object` | yes | Not declared |
| `created_at` | `string` | no | Not declared |
| `errors` | `array` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `limitations` | `array` | no | Not declared |
| `passed` | `boolean` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `static_analysis_only` | `Not declared` | yes | Not declared |
| `supplied_code_executed` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

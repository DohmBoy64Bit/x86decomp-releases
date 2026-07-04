---
title: "release-gate.schema.json"
description: "Exact source-derived schema reference for schemas/release-gate.schema.json"
---

# `schemas/release-gate.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/release-gate.schema.json` |
| SHA-256 | `50e1f5a6cb46b67f833c881a7f025be5c7c047c1f23c3607608488afe17256cd` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:release-gate:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `created_at`
- `project_root`
- `checks`
- `requirements`
- `failures`
- `passed`
- `truth_statement`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `checks` | `object` | yes | Not declared |
| `created_at` | `string` | yes | Not declared |
| `failures` | `array` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `passed` | `boolean` | yes | Not declared |
| `project_root` | `string` | yes | Not declared |
| `requirements` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `truth_statement` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

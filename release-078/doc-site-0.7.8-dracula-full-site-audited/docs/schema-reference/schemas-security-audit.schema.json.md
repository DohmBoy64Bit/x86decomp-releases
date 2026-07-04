---
title: "security-audit.schema.json"
description: "Exact source-derived schema reference for schemas/security-audit.schema.json"
---

# `schemas/security-audit.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/security-audit.schema.json` |
| SHA-256 | `d62a14bd5c6d796dd52aee929ccfdf8e1265f825167070c8ffd680321a00b637` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:security-audit:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 11 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

## Required fields

- `schema_version`
- `kind`
- `root`
- `file_count`
- `findings`
- `severity_counts`
- `passed`
- `vulnerability_database_checked`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `created_at` | `string` | no | Not declared |
| `file_count` | `integer` | yes | Not declared |
| `findings` | `array` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `limitations` | `array` | no | Not declared |
| `passed` | `boolean` | yes | Not declared |
| `root` | `string` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `severity_counts` | `object` | yes | Not declared |
| `total_bytes` | `integer` | no | Not declared |
| `vulnerability_database_checked` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

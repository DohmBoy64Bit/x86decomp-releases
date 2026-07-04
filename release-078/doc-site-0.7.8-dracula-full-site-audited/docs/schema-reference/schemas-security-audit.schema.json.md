---
title: "security-audit.schema.json"
description: "Schema reference for schemas/security-audit.schema.json"
---

# `schemas/security-audit.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/security-audit.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:security-audit:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 11 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

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
| `created_at` | `string` | no | — |
| `file_count` | `integer` | yes | — |
| `findings` | `array` | yes | — |
| `kind` | — | yes | — |
| `limitations` | `array` | no | — |
| `passed` | `boolean` | yes | — |
| `root` | `string` | yes | — |
| `schema_version` | — | yes | — |
| `severity_counts` | `object` | yes | — |
| `total_bytes` | `integer` | no | — |
| `vulnerability_database_checked` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


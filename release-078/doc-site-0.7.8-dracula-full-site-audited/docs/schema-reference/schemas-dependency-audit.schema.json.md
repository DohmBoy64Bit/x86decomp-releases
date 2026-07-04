---
title: "x86decomp dependency vulnerability audit"
description: "Schema reference for schemas/dependency-audit.schema.json"
---

# `schemas/dependency-audit.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/dependency-audit.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:dependency-audit:1` |
| Title | x86decomp dependency vulnerability audit |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 11 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `created_at`
- `tool`
- `tool_sha256`
- `return_code`
- `dependency_count`
- `vulnerability_count`
- `vulnerabilities`
- `passed`
- `raw_report`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `created_at` | `string` | yes | — |
| `dependency_count` | `integer` | yes | — |
| `kind` | — | yes | — |
| `passed` | `boolean` | yes | — |
| `raw_report` | — | yes | — |
| `return_code` | `integer` | yes | — |
| `schema_version` | — | yes | — |
| `stderr` | `string` | no | — |
| `tool` | `string` | yes | — |
| `tool_sha256` | `string` | yes | — |
| `vulnerabilities` | `array` | yes | — |
| `vulnerability_count` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "release-gate.schema.json"
description: "Schema reference for schemas/release-gate.schema.json"
---

# `schemas/release-gate.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/release-gate.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:release-gate:1` |
| Title | — |
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
| `checks` | `object` | yes | — |
| `created_at` | `string` | yes | — |
| `failures` | `array` | yes | — |
| `kind` | — | yes | — |
| `passed` | `boolean` | yes | — |
| `project_root` | `string` | yes | — |
| `requirements` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `truth_statement` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


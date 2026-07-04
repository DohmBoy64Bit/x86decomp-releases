---
title: "Normalized DynamoRIO drcov text trace"
description: "Schema reference for schemas/drcov-trace.schema.json"
---

# `schemas/drcov-trace.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/drcov-trace.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:drcov-trace:1` |
| Title | Normalized DynamoRIO drcov text trace |
| Top-level type | `object` |
| Top-level properties | 10 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `kind`
- `source`
- `source_sha256`
- `drcov_version`
- `modules`
- `basic_blocks`
- `unique_basic_blocks`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `basic_blocks` | `array` | yes | — |
| `drcov_flavor` | `string, null` | no | — |
| `drcov_version` | `string` | yes | — |
| `kind` | — | yes | — |
| `module_table_version` | `integer, null` | no | — |
| `modules` | `array` | yes | — |
| `schema_version` | — | yes | — |
| `source` | `string` | yes | — |
| `source_sha256` | `string` | yes | — |
| `unique_basic_blocks` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


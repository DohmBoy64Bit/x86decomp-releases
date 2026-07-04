---
title: "Normalized DynamoRIO drcov text trace"
description: "Exact source-derived schema reference for schemas/drcov-trace.schema.json"
---

# `schemas/drcov-trace.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/drcov-trace.schema.json` |
| SHA-256 | `aedc8ab92612b4b325552d3de98da9d04e2e4c3aa2bb2ab319e20f85616cfe7f` |
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
| `basic_blocks` | `array` | yes | Not declared |
| `drcov_flavor` | `string, null` | no | Not declared |
| `drcov_version` | `string` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `module_table_version` | `integer, null` | no | Not declared |
| `modules` | `array` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `source` | `string` | yes | Not declared |
| `source_sha256` | `string` | yes | Not declared |
| `unique_basic_blocks` | `integer` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

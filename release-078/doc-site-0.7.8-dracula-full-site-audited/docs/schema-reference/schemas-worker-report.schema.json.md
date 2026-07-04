---
title: "worker-report.schema.json"
description: "Schema reference for schemas/worker-report.schema.json"
---

# `schemas/worker-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/worker-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:worker-report:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 15 |
| Required fields | 7 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

## Required fields

- `schema_version`
- `status`
- `command`
- `isolation`
- `isolation_strength`
- `input_hashes`
- `output_hashes`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `command` | `array` | yes | — |
| `duration_seconds` | `number` | no | — |
| `error` | `string, null` | no | — |
| `input_hashes` | `object` | yes | — |
| `isolation` | — | yes | — |
| `isolation_strength` | `string` | yes | — |
| `output_hashes` | `object` | yes | — |
| `returncode` | `integer, null` | no | — |
| `schema_version` | — | yes | — |
| `started_at` | `string` | no | — |
| `status` | — | yes | — |
| `stderr_path` | `string` | no | — |
| `stderr_truncated` | `boolean` | no | — |
| `stdout_path` | `string` | no | — |
| `stdout_truncated` | `boolean` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


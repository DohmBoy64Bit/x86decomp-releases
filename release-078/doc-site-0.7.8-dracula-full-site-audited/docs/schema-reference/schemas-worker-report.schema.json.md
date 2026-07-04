---
title: "worker-report.schema.json"
description: "Exact source-derived schema reference for schemas/worker-report.schema.json"
---

# `schemas/worker-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/worker-report.schema.json` |
| SHA-256 | `f4fee8d629c5e963519a4f5ab25c4bb0856592421ee218fe7d047b5ebe089b3c` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:worker-report:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 15 |
| Required fields | 7 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

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
| `command` | `array` | yes | Not declared |
| `duration_seconds` | `number` | no | Not declared |
| `error` | `string, null` | no | Not declared |
| `input_hashes` | `object` | yes | Not declared |
| `isolation` | `Not declared` | yes | Not declared |
| `isolation_strength` | `string` | yes | Not declared |
| `output_hashes` | `object` | yes | Not declared |
| `returncode` | `integer, null` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `started_at` | `string` | no | Not declared |
| `status` | `Not declared` | yes | Not declared |
| `stderr_path` | `string` | no | Not declared |
| `stderr_truncated` | `boolean` | no | Not declared |
| `stdout_path` | `string` | no | Not declared |
| `stdout_truncated` | `boolean` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

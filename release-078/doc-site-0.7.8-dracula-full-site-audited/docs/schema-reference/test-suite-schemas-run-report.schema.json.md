---
title: "x86decomp comprehensive test run report"
description: "Schema reference for test-suite/schemas/run-report.schema.json"
---

# `test-suite/schemas/run-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `test-suite` |
| Source path | `test-suite/schemas/run-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp-test-suite:run-report:1` |
| Title | x86decomp comprehensive test run report |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 13 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `run_id`
- `toolkit_root`
- `output_directory`
- `strict`
- `started_at`
- `finished_at`
- `adapter_results`
- `test_results`
- `inventory`
- `configuration`
- `counts`
- `exit_code`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `adapter_results` | `array` | yes | — |
| `counts` | `object` | yes | — |
| `exit_code` | — | yes | — |
| `output_directory` | `string` | yes | — |
| `run_id` | `string` | yes | — |
| `schema_version` | — | yes | — |
| `strict` | `boolean` | yes | — |
| `test_results` | `array` | yes | — |
| `toolkit_root` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


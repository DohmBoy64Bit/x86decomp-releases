---
title: "x86decomp comprehensive test run report"
description: "Exact source-derived schema reference for test-suite/schemas/run-report.schema.json"
---

# `test-suite/schemas/run-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `test-suite` |
| Source path | `test-suite/schemas/run-report.schema.json` |
| SHA-256 | `9d2b3fcab807e52866a5b8e7bac9f7813e6d7e003d4de9f2f80d05e8798e93c6` |
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
| `adapter_results` | `array` | yes | Not declared |
| `counts` | `object` | yes | Not declared |
| `exit_code` | `Not declared` | yes | Not declared |
| `output_directory` | `string` | yes | Not declared |
| `run_id` | `string` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `strict` | `boolean` | yes | Not declared |
| `test_results` | `array` | yes | Not declared |
| `toolkit_root` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

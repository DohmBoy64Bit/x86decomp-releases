---
title: "x86decomp test configuration"
description: "Exact source-derived schema reference for test-suite/schemas/test-config.schema.json"
---

# `test-suite/schemas/test-config.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `test-suite` |
| Source path | `test-suite/schemas/test-config.schema.json` |
| SHA-256 | `c33b8ab58a509c7f688ff159d0cef5726a4909801d40fd4899c81c4626eda90d` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp-test-suite:test-config:1` |
| Title | x86decomp test configuration |
| Top-level type | `object` |
| Top-level properties | 16 |
| Required fields | 15 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `toolkit_root`
- `output_root`
- `adapter_paths`
- `python_executable`
- `strict`
- `interactive`
- `allow_network`
- `allow_install`
- `allow_host_execution`
- `timeout_seconds`
- `line_coverage_floor`
- `branch_coverage_floor`
- `require_public_api_execution`
- `custom_environment`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `adapter_paths` | `object` | yes | Not declared |
| `allow_host_execution` | `boolean` | yes | Not declared |
| `allow_install` | `boolean` | yes | Not declared |
| `allow_network` | `boolean` | yes | Not declared |
| `branch_coverage_floor` | `number` | yes | Not declared |
| `custom_environment` | `object` | yes | Not declared |
| `install_root` | `string, null` | no | Not declared |
| `interactive` | `boolean` | yes | Not declared |
| `line_coverage_floor` | `number` | yes | Not declared |
| `output_root` | `string` | yes | Not declared |
| `python_executable` | `string` | yes | Not declared |
| `require_public_api_execution` | `boolean` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `strict` | `boolean` | yes | Not declared |
| `timeout_seconds` | `integer` | yes | Not declared |
| `toolkit_root` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

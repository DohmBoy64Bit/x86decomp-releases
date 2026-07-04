---
title: "x86decomp test configuration"
description: "Schema reference for test-suite/schemas/test-config.schema.json"
---

# `test-suite/schemas/test-config.schema.json`

| Field | Value |
| --- | --- |
| Scope | `test-suite` |
| Source path | `test-suite/schemas/test-config.schema.json` |
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
| `adapter_paths` | `object` | yes | — |
| `allow_host_execution` | `boolean` | yes | — |
| `allow_install` | `boolean` | yes | — |
| `allow_network` | `boolean` | yes | — |
| `branch_coverage_floor` | `number` | yes | — |
| `custom_environment` | `object` | yes | — |
| `install_root` | `string, null` | no | — |
| `interactive` | `boolean` | yes | — |
| `line_coverage_floor` | `number` | yes | — |
| `output_root` | `string` | yes | — |
| `python_executable` | `string` | yes | — |
| `require_public_api_execution` | `boolean` | yes | — |
| `schema_version` | — | yes | — |
| `strict` | `boolean` | yes | — |
| `timeout_seconds` | `integer` | yes | — |
| `toolkit_root` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


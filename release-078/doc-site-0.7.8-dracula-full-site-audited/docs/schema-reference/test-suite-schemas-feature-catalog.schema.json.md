---
title: "x86decomp current-surface catalog"
description: "Exact source-derived schema reference for test-suite/schemas/feature-catalog.schema.json"
---

# `test-suite/schemas/feature-catalog.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `test-suite` |
| Source path | `test-suite/schemas/feature-catalog.schema.json` |
| SHA-256 | `554a6d8ef19025ff91c877be73c541678bebf2b13026d91bf7eba28ddef5a278` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp-test-suite:feature-catalog:1` |
| Title | x86decomp current-surface catalog |
| Top-level type | `object` |
| Top-level properties | 14 |
| Required fields | 14 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `toolkit_version`
- `entry_points`
- `modules`
- `all_function_symbols`
- `cli_commands`
- `canonical_groups`
- `canonical_routes`
- `schemas`
- `ghidra_scripts`
- `workflow_states`
- `adapters`
- `coverage_contract`
- `maintenance_rule`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `adapters` | `array` | yes | Not declared |
| `all_function_symbols` | `array` | yes | Not declared |
| `canonical_groups` | `array` | yes | Not declared |
| `canonical_routes` | `array` | yes | Not declared |
| `cli_commands` | `object` | yes | Not declared |
| `coverage_contract` | `object` | yes | Not declared |
| `entry_points` | `object` | yes | Not declared |
| `ghidra_scripts` | `array` | yes | Not declared |
| `maintenance_rule` | `string` | yes | Not declared |
| `modules` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `schemas` | `array` | yes | Not declared |
| `toolkit_version` | `Not declared` | yes | Not declared |
| `workflow_states` | `object` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

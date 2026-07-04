---
title: "x86decomp current-surface catalog"
description: "Schema reference for test-suite/schemas/feature-catalog.schema.json"
---

# `test-suite/schemas/feature-catalog.schema.json`

| Field | Value |
| --- | --- |
| Scope | `test-suite` |
| Source path | `test-suite/schemas/feature-catalog.schema.json` |
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
| `adapters` | `array` | yes | — |
| `all_function_symbols` | `array` | yes | — |
| `canonical_groups` | `array` | yes | — |
| `canonical_routes` | `array` | yes | — |
| `cli_commands` | `object` | yes | — |
| `coverage_contract` | `object` | yes | — |
| `entry_points` | `object` | yes | — |
| `ghidra_scripts` | `array` | yes | — |
| `maintenance_rule` | `string` | yes | — |
| `modules` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `schemas` | `array` | yes | — |
| `toolkit_version` | — | yes | — |
| `workflow_states` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


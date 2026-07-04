---
title: "Operator-confirmed target decisions"
description: "Schema reference for schemas/target-decisions.schema.json"
---

# `schemas/target-decisions.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/target-decisions.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:target-decisions:1` |
| Title | Operator-confirmed target decisions |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 7 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `preferred_mode`
- `compiler_family`
- `compiler_version`
- `linker_family`
- `source_language`
- `allow_host_execution`
- `target_description`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `allow_host_execution` | `boolean` | yes | — |
| `compiler_family` | `string` | yes | — |
| `compiler_version` | `string` | yes | — |
| `linker_family` | `string` | yes | — |
| `preferred_mode` | — | yes | — |
| `source_language` | — | yes | — |
| `target_description` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


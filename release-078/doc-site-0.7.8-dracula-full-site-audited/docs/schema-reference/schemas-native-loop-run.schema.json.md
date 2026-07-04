---
title: "x86decomp loop-run"
description: "Schema reference for schemas/native/loop-run.schema.json"
---

# `schemas/native/loop-run.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/loop-run.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.invalid/schemas/native/loop-run.schema.json` |
| Title | x86decomp loop-run |
| Top-level type | `object` |
| Top-level properties | 4 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `function_id`
- `source_path`
- `compile_command`
- `candidate_path`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate_path` | `string` | yes | — |
| `compile_command` | `array` | yes | — |
| `function_id` | `string` | yes | — |
| `source_path` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "x86decomp loop-run"
description: "Exact source-derived schema reference for schemas/native/loop-run.schema.json"
---

# `schemas/native/loop-run.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/loop-run.schema.json` |
| SHA-256 | `de5d1a277444c3ea53ae0c4860d1a7978b478893fb893cf4c1ba1fca4a11b038` |
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
| `candidate_path` | `string` | yes | Not declared |
| `compile_command` | `array` | yes | Not declared |
| `function_id` | `string` | yes | Not declared |
| `source_path` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

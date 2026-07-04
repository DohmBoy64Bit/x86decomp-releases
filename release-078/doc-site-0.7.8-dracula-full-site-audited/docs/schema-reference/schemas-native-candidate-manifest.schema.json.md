---
title: "x86decomp candidate-manifest"
description: "Exact source-derived schema reference for schemas/native/candidate-manifest.schema.json"
---

# `schemas/native/candidate-manifest.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/native/candidate-manifest.schema.json` |
| SHA-256 | `d3bad2e693b4b7d6e1c230d9e03ff775298273523c8b562d3b78400c13313029` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.invalid/schemas/native/candidate-manifest.schema.json` |
| Title | x86decomp candidate-manifest |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `function_id`
- `rva`
- `slot_size`
- `candidate_path`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate_path` | `string` | yes | Not declared |
| `function_id` | `string` | yes | Not declared |
| `rva` | `oneOf` | yes | Not declared |
| `slot_size` | `integer` | yes | Not declared |
| `symbol` | `string, null` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

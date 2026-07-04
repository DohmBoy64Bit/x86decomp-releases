---
title: "Compiler ground-truth corpus manifest"
description: "Exact source-derived schema reference for schemas/compiler-ground-truth.schema.json"
---

# `schemas/compiler-ground-truth.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/compiler-ground-truth.schema.json` |
| SHA-256 | `1f8d15358ce71168a0f7c4d61ba7ad9db1ef12b534b27444bdda1f77f96392a2` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:compiler-ground-truth:1` |
| Title | Compiler ground-truth corpus manifest |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 3 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `compilers`
- `cases`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `cases` | `array` | yes | Not declared |
| `compilers` | `array` | yes | Not declared |
| `flag_matrix` | `object` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `timeout_seconds` | `integer` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

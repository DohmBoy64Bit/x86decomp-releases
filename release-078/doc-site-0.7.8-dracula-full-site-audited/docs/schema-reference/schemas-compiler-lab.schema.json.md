---
title: "Compiler experiment matrix"
description: "Exact source-derived schema reference for schemas/compiler-lab.schema.json"
---

# `schemas/compiler-lab.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/compiler-lab.schema.json` |
| SHA-256 | `37bc55f945daffc31844a78c2b4788191f501589303826a6cee207c5c4717506` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:compiler-lab:1` |
| Title | Compiler experiment matrix |
| Top-level type | `object` |
| Top-level properties | 8 |
| Required fields | 2 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `source`
- `profiles`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `cache_root` | `string` | no | Not declared |
| `matrix` | `object` | no | Not declared |
| `max_experiments` | `integer` | no | Not declared |
| `output_name` | `string` | no | Not declared |
| `output_root` | `string` | no | Not declared |
| `profiles` | `array` | yes | Not declared |
| `source` | `string` | yes | Not declared |
| `target` | `oneOf` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

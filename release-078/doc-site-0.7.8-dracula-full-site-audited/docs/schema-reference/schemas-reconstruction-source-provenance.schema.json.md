---
title: "Source provenance record"
description: "Exact source-derived schema reference for schemas/reconstruction/source-provenance.schema.json"
---

# `schemas/reconstruction/source-provenance.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/source-provenance.schema.json` |
| SHA-256 | `d80a00434549c01f14f1afa7c43cb65b9eb653808b42fb5fa10f25b1d7ac1b0c` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/source-provenance.schema.json` |
| Title | Source provenance record |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `provenance_id`
- `source_path`
- `line_start`
- `line_end`
- `binary_id`
- `address_start`
- `address_end`
- `evidence`
- `confidence`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `address_end` | `string` | yes | Not declared |
| `address_start` | `string` | yes | Not declared |
| `binary_id` | `string` | yes | Not declared |
| `confidence` | `number` | yes | Not declared |
| `evidence` | `array` | yes | Not declared |
| `line_end` | `integer` | yes | Not declared |
| `line_start` | `integer` | yes | Not declared |
| `provenance_id` | `string` | yes | Not declared |
| `source_path` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

---
title: "Source provenance record"
description: "Schema reference for schemas/reconstruction/source-provenance.schema.json"
---

# `schemas/reconstruction/source-provenance.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/source-provenance.schema.json` |
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
| `address_end` | `string` | yes | — |
| `address_start` | `string` | yes | — |
| `binary_id` | `string` | yes | — |
| `confidence` | `number` | yes | — |
| `evidence` | `array` | yes | — |
| `line_end` | `integer` | yes | — |
| `line_start` | `integer` | yes | — |
| `provenance_id` | `string` | yes | — |
| `source_path` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


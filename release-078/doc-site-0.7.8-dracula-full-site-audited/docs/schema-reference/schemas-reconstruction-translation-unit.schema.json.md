---
title: "Translation unit hypothesis"
description: "Schema reference for schemas/reconstruction/translation-unit.schema.json"
---

# `schemas/reconstruction/translation-unit.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/translation-unit.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/translation-unit.schema.json` |
| Title | Translation unit hypothesis |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `unit_id`
- `source_path`
- `language`
- `confidence`
- `evidence`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `confidence` | `number` | yes | — |
| `evidence` | `array` | yes | — |
| `language` | — | yes | — |
| `source_path` | `string` | yes | — |
| `unit_id` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


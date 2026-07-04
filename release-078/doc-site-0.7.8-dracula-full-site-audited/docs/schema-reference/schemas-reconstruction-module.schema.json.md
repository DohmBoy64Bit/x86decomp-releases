---
title: "Recovered module hypothesis"
description: "Schema reference for schemas/reconstruction/module.schema.json"
---

# `schemas/reconstruction/module.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/module.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/module.schema.json` |
| Title | Recovered module hypothesis |
| Top-level type | `object` |
| Top-level properties | 6 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `module_id`
- `name`
- `kind`
- `confidence`
- `evidence`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `confidence` | `number` | yes | — |
| `evidence` | `array` | yes | — |
| `kind` | — | yes | — |
| `module_id` | `string` | yes | — |
| `name` | `string` | yes | — |
| `source_path` | `string, null` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "Continuously buildable hybrid project"
description: "Schema reference for schemas/hybrid-project.schema.json"
---

# `schemas/hybrid-project.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/hybrid-project.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:hybrid-project:1` |
| Title | Continuously buildable hybrid project |
| Top-level type | `object` |
| Top-level properties | 6 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `created_at`
- `project_root`
- `architecture`
- `functions`
- `build`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `build` | `object` | yes | — |
| `created_at` | `string` | yes | — |
| `functions` | `array` | yes | — |
| `project_root` | `string` | yes | — |
| `schema_version` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


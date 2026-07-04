---
title: "reproduction.schema.json"
description: "Schema reference for schemas/reproduction.schema.json"
---

# `schemas/reproduction.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reproduction.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:reproduction:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | — |

## Required fields

- `schema_version`
- `project_id`
- `project_schema_version`
- `binary`
- `critical_files`
- `tools`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `binary` | `object` | yes | — |
| `content_store` | `object, null` | no | — |
| `created_at` | `string` | no | — |
| `critical_files` | `array` | yes | — |
| `host` | `object` | no | — |
| `limitations` | `array` | no | — |
| `project_check` | `object` | no | — |
| `project_id` | `string` | yes | — |
| `project_schema_version` | `integer` | yes | — |
| `schema_version` | — | yes | — |
| `target_pack_check` | `object, null` | no | — |
| `toolkit_release` | `string` | no | — |
| `tools` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


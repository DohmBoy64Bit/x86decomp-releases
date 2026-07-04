---
title: "target-pack.schema.json"
description: "Schema reference for schemas/target-pack.schema.json"
---

# `schemas/target-pack.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/target-pack.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:target-pack:1` |
| Title | — |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 12 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `target_id`
- `name`
- `created_at`
- `architecture`
- `image_kind`
- `primary_image`
- `primary_sha256`
- `default_modes`
- `scope`
- `decisions`
- `artifacts`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `artifacts` | `array` | yes | — |
| `created_at` | `string` | yes | — |
| `decisions` | `object` | yes | — |
| `default_modes` | — | yes | — |
| `image_kind` | — | yes | — |
| `name` | `string` | yes | — |
| `primary_image` | `string` | yes | — |
| `primary_sha256` | `string` | yes | — |
| `schema_version` | — | yes | — |
| `scope` | `object` | yes | — |
| `target_id` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


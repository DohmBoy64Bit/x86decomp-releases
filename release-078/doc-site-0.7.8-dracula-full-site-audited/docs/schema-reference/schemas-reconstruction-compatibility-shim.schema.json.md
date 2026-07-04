---
title: "Explicit compatibility shim"
description: "Schema reference for schemas/reconstruction/compatibility-shim.schema.json"
---

# `schemas/reconstruction/compatibility-shim.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/compatibility-shim.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/compatibility-shim.schema.json` |
| Title | Explicit compatibility shim |
| Top-level type | `object` |
| Top-level properties | 6 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `shim_id`
- `subject_id`
- `shim_kind`
- `source_path`
- `contract`
- `status`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `contract` | `object` | yes | — |
| `shim_id` | `string` | yes | — |
| `shim_kind` | — | yes | — |
| `source_path` | `string` | yes | — |
| `status` | `string` | yes | — |
| `subject_id` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


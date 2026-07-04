---
title: "Manifest-driven full relink"
description: "Schema reference for schemas/relink-manifest.schema.json"
---

# `schemas/relink-manifest.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/relink-manifest.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:relink-manifest:1` |
| Title | Manifest-driven full relink |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 7 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `linker`
- `objects`
- `output`
- `arguments`
- `environment`
- `timeout_seconds`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `arguments` | `array` | yes | — |
| `environment` | `object` | yes | — |
| `inherit_environment` | `boolean` | no | — |
| `linker` | `string` | yes | — |
| `objects` | `array` | yes | — |
| `output` | `string` | yes | — |
| `reference_image` | `string` | no | — |
| `schema_version` | — | yes | — |
| `timeout_seconds` | `integer` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "Target-specific PE image layout profile"
description: "Schema reference for schemas/image-profile.schema.json"
---

# `schemas/image-profile.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/image-profile.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:image-profile:1` |
| Title | Target-specific PE image layout profile |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `reference_sha256`
- `architecture`
- `section_order`
- `normalization`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `entry_rva` | `integer` | no | — |
| `image_base` | `integer` | no | — |
| `kind` | — | yes | — |
| `normalization` | `object` | yes | — |
| `reference_sha256` | `string` | yes | — |
| `schema_version` | — | yes | — |
| `section_order` | `array` | yes | — |
| `sections` | `array` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


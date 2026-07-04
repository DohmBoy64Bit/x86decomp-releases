---
title: "Target-specific PE image layout profile"
description: "Exact source-derived schema reference for schemas/image-profile.schema.json"
---

# `schemas/image-profile.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/image-profile.schema.json` |
| SHA-256 | `5916e3589fb77876a26861ccfea7dfbfbf4b9c55e92243ed66dae4270dad70d7` |
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
| `architecture` | `Not declared` | yes | Not declared |
| `entry_rva` | `integer` | no | Not declared |
| `image_base` | `integer` | no | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `normalization` | `object` | yes | Not declared |
| `reference_sha256` | `string` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `section_order` | `array` | yes | Not declared |
| `sections` | `array` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

---
title: "Manifest-driven full relink"
description: "Exact source-derived schema reference for schemas/relink-manifest.schema.json"
---

# `schemas/relink-manifest.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/relink-manifest.schema.json` |
| SHA-256 | `ca2b77b7be6b562589e841753a9afa8c6baf1fc7cf8c703409c90fc56507e890` |
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
| `arguments` | `array` | yes | Not declared |
| `environment` | `object` | yes | Not declared |
| `inherit_environment` | `boolean` | no | Not declared |
| `linker` | `string` | yes | Not declared |
| `objects` | `array` | yes | Not declared |
| `output` | `string` | yes | Not declared |
| `reference_image` | `string` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `timeout_seconds` | `integer` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

---
title: "reproduction.schema.json"
description: "Exact source-derived schema reference for schemas/reproduction.schema.json"
---

# `schemas/reproduction.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reproduction.schema.json` |
| SHA-256 | `aea350be271c7795406a2dd55096775e9d0b531215e05f43b75a9c6b5bd98281` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:reproduction:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | Not declared |

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
| `binary` | `object` | yes | Not declared |
| `content_store` | `object, null` | no | Not declared |
| `created_at` | `string` | no | Not declared |
| `critical_files` | `array` | yes | Not declared |
| `host` | `object` | no | Not declared |
| `limitations` | `array` | no | Not declared |
| `project_check` | `object` | no | Not declared |
| `project_id` | `string` | yes | Not declared |
| `project_schema_version` | `integer` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `target_pack_check` | `object, null` | no | Not declared |
| `toolkit_release` | `string` | no | Not declared |
| `tools` | `object` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

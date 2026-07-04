---
title: "x86decomp compiler profile"
description: "Exact source-derived schema reference for schemas/compiler-profile.schema.json"
---

# `schemas/compiler-profile.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/compiler-profile.schema.json` |
| SHA-256 | `6903f160acf5cfb8329567efbdd2da82b9f171705971e9842afcae21a4a4f844` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:compiler-profile:2` |
| Title | x86decomp compiler profile |
| Top-level type | `object` |
| Top-level properties | 14 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `id`
- `description`
- `executable`
- `language`
- `output_kind`
- `timeout_seconds`
- `arguments`
- `environment`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `arguments` | `array` | yes | Not declared |
| `command_prefix` | `array` | no | Not declared |
| `description` | `string` | yes | Not declared |
| `environment` | `object` | yes | Not declared |
| `executable` | `string` | yes | Not declared |
| `family` | `string, null` | no | Not declared |
| `id` | `string` | yes | Not declared |
| `inherit_environment` | `boolean` | no | Not declared |
| `language` | `Not declared` | yes | Not declared |
| `output_kind` | `Not declared` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `timeout_seconds` | `integer` | yes | Not declared |
| `version` | `string, null` | no | Not declared |
| `version_arguments` | `array` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

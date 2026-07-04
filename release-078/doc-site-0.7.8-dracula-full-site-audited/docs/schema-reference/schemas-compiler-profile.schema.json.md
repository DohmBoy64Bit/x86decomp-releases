---
title: "x86decomp compiler profile"
description: "Schema reference for schemas/compiler-profile.schema.json"
---

# `schemas/compiler-profile.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/compiler-profile.schema.json` |
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
| `arguments` | `array` | yes | — |
| `command_prefix` | `array` | no | — |
| `description` | `string` | yes | — |
| `environment` | `object` | yes | — |
| `executable` | `string` | yes | — |
| `family` | `string, null` | no | — |
| `id` | `string` | yes | — |
| `inherit_environment` | `boolean` | no | — |
| `language` | — | yes | — |
| `output_kind` | — | yes | — |
| `schema_version` | — | yes | — |
| `timeout_seconds` | `integer` | yes | — |
| `version` | `string, null` | no | — |
| `version_arguments` | `array` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


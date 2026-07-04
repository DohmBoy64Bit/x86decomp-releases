---
title: "Local decomp.me-style function packet"
description: "Schema reference for schemas/decompme-packet.schema.json"
---

# `schemas/decompme-packet.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/decompme-packet.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:decompme-packet:1` |
| Title | Local decomp.me-style function packet |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `created_at`
- `kind`
- `function_id`
- `source_artifact`
- `output_directory`
- `files`
- `uploaded`
- `limitations`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `created_at` | `string` | yes | — |
| `files` | `array` | yes | — |
| `function_id` | `string` | yes | — |
| `kind` | — | yes | — |
| `limitations` | `array` | yes | — |
| `output_directory` | `string` | yes | — |
| `schema_version` | — | yes | — |
| `source_artifact` | `string` | yes | — |
| `uploaded` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


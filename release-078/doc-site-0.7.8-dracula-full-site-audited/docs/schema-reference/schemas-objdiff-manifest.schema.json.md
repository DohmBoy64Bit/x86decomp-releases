---
title: "objdiff external invocation manifest"
description: "Schema reference for schemas/objdiff-manifest.schema.json"
---

# `schemas/objdiff-manifest.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/objdiff-manifest.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:objdiff-manifest:1` |
| Title | objdiff external invocation manifest |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `target`
- `candidate`
- `arguments`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `arguments` | `array` | yes | — |
| `candidate` | `string` | yes | — |
| `environment` | `object` | no | — |
| `executable` | `string` | no | — |
| `inherit_environment` | `boolean` | no | — |
| `output` | `string` | no | — |
| `output_format` | — | no | — |
| `require_output` | `boolean` | no | — |
| `schema_version` | — | yes | — |
| `success_exit_codes` | `array` | no | — |
| `target` | `string` | yes | — |
| `timeout_seconds` | `integer` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


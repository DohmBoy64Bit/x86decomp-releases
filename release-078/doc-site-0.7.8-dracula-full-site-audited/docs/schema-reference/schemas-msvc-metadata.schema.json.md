---
title: "Bounded MSVC metadata analysis report"
description: "Schema reference for schemas/msvc-metadata.schema.json"
---

# `schemas/msvc-metadata.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/msvc-metadata.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:msvc-metadata:1` |
| Title | Bounded MSVC metadata analysis report |
| Top-level type | `object` |
| Top-level properties | 8 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `image`
- `rtti`
- `exceptions`
- `tls`
- `static_initializers`
- `source_level_recovery_claimed`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `exceptions` | `object` | yes | — |
| `image` | `object` | yes | — |
| `kind` | — | yes | — |
| `rtti` | `object` | yes | — |
| `schema_version` | — | yes | — |
| `source_level_recovery_claimed` | — | yes | — |
| `static_initializers` | `object` | yes | — |
| `tls` | `object, null` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


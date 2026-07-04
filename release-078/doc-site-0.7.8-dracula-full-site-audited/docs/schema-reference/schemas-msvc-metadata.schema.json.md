---
title: "Bounded MSVC metadata analysis report"
description: "Exact source-derived schema reference for schemas/msvc-metadata.schema.json"
---

# `schemas/msvc-metadata.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/msvc-metadata.schema.json` |
| SHA-256 | `84d0b6bc880ab47954f951a4eed4db317c14ee33ed5cdbe0ee098ce61c1d6273` |
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
| `exceptions` | `object` | yes | Not declared |
| `image` | `object` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `rtti` | `object` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `source_level_recovery_claimed` | `Not declared` | yes | Not declared |
| `static_initializers` | `object` | yes | Not declared |
| `tls` | `object, null` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

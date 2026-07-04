---
title: "x86decomp COFF Archive Inspection"
description: "Schema reference for schemas/coff-archive.schema.json"
---

# `schemas/coff-archive.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/coff-archive.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:coff-archive:1` |
| Title | x86decomp COFF Archive Inspection |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 7 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `format`
- `source_path`
- `source_sha256`
- `member_count`
- `members`
- `linker_symbols`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `format` | — | yes | — |
| `linker_symbols` | `array` | yes | — |
| `member_count` | `integer` | yes | — |
| `members` | `array` | yes | — |
| `schema_version` | — | yes | — |
| `source_path` | `string, null` | yes | — |
| `source_sha256` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


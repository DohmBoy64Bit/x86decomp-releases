---
title: "x86decomp COFF Archive Inspection"
description: "Exact source-derived schema reference for schemas/coff-archive.schema.json"
---

# `schemas/coff-archive.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/coff-archive.schema.json` |
| SHA-256 | `5f5a43f1ce6ae1221df24107f7b9db057156731736ff4aad5c81c93a73abaab3` |
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
| `format` | `Not declared` | yes | Not declared |
| `linker_symbols` | `array` | yes | Not declared |
| `member_count` | `integer` | yes | Not declared |
| `members` | `array` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `source_path` | `string, null` | yes | Not declared |
| `source_sha256` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

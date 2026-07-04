---
title: "x86decomp bounded PDB/MSF inventory"
description: "Exact source-derived schema reference for schemas/pdb.schema.json"
---

# `schemas/pdb.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/pdb.schema.json` |
| SHA-256 | `850bbf885fa040ac4601dc4d93c2fb4b3afda1dd86612a0d8866a34bacf07008` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:pdb:1` |
| Title | x86decomp bounded PDB/MSF inventory |
| Top-level type | `object` |
| Top-level properties | 13 |
| Required fields | 13 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `format`
- `source_path`
- `source_sha256`
- `superblock`
- `stream_count`
- `streams`
- `pdb_info`
- `tpi`
- `ipi`
- `dbi`
- `pe_match`
- `scope`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `dbi` | `object, null` | yes | Not declared |
| `format` | `Not declared` | yes | Not declared |
| `ipi` | `object, null` | yes | Not declared |
| `pdb_info` | `object, null` | yes | Not declared |
| `pe_match` | `object, null` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `scope` | `object` | yes | Not declared |
| `source_path` | `string, null` | yes | Not declared |
| `source_sha256` | `string` | yes | Not declared |
| `stream_count` | `integer` | yes | Not declared |
| `streams` | `array` | yes | Not declared |
| `superblock` | `object` | yes | Not declared |
| `tpi` | `object, null` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

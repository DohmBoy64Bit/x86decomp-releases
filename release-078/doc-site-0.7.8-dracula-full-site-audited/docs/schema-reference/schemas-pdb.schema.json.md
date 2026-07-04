---
title: "x86decomp bounded PDB/MSF inventory"
description: "Schema reference for schemas/pdb.schema.json"
---

# `schemas/pdb.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/pdb.schema.json` |
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
| `dbi` | `object, null` | yes | — |
| `format` | — | yes | — |
| `ipi` | `object, null` | yes | — |
| `pdb_info` | `object, null` | yes | — |
| `pe_match` | `object, null` | yes | — |
| `schema_version` | — | yes | — |
| `scope` | `object` | yes | — |
| `source_path` | `string, null` | yes | — |
| `source_sha256` | `string` | yes | — |
| `stream_count` | `integer` | yes | — |
| `streams` | `array` | yes | — |
| `superblock` | `object` | yes | — |
| `tpi` | `object, null` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "v0.7.8 mnemonic round-trip report"
description: "Schema reference for schemas/assembly/roundtrip-report.schema.json"
---

# `schemas/assembly/roundtrip-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/assembly/roundtrip-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/assembly/roundtrip-report.schema.json` |
| Title | v0.7.8 mnemonic round-trip report |
| Top-level type | `object` |
| Top-level properties | 10 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `source`
- `object`
- `symbol`
- `rva`
- `architecture`
- `input_sha256`
- `resolved_sha256`
- `exact_match`
- `classification`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `classification` | — | yes | — |
| `exact_match` | `boolean` | yes | — |
| `input_sha256` | `string` | yes | — |
| `object` | `string` | yes | — |
| `resolved_sha256` | `string` | yes | — |
| `rva` | `integer` | yes | — |
| `semantic_equivalence_claimed` | — | no | — |
| `source` | `string` | yes | — |
| `symbol` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


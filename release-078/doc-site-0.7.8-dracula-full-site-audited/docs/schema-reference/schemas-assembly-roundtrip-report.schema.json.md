---
title: "v0.7.8 mnemonic round-trip report"
description: "Exact source-derived schema reference for schemas/assembly/roundtrip-report.schema.json"
---

# `schemas/assembly/roundtrip-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/assembly/roundtrip-report.schema.json` |
| SHA-256 | `00ecc65165836a423b5f53482d5367d4a70b88891dda997f0da0b6bd854ac1ac` |
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
| `architecture` | `Not declared` | yes | Not declared |
| `classification` | `Not declared` | yes | Not declared |
| `exact_match` | `boolean` | yes | Not declared |
| `input_sha256` | `string` | yes | Not declared |
| `object` | `string` | yes | Not declared |
| `resolved_sha256` | `string` | yes | Not declared |
| `rva` | `integer` | yes | Not declared |
| `semantic_equivalence_claimed` | `Not declared` | no | Not declared |
| `source` | `string` | yes | Not declared |
| `symbol` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

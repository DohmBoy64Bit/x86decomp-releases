---
title: "Deterministic synthetic source corpus"
description: "Schema reference for schemas/synthetic-corpus.schema.json"
---

# `schemas/synthetic-corpus.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/synthetic-corpus.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:synthetic-corpus:1` |
| Title | Deterministic synthetic source corpus |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `kind`
- `created_at`
- `seed`
- `cases_per_family`
- `families`
- `case_count`
- `cases`
- `truth_scope`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `case_count` | `integer` | yes | — |
| `cases` | `array` | yes | — |
| `cases_per_family` | `integer` | yes | — |
| `created_at` | `string` | yes | — |
| `families` | `array` | yes | — |
| `kind` | — | yes | — |
| `schema_version` | — | yes | — |
| `seed` | `integer` | yes | — |
| `truth_scope` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "Deterministic synthetic source corpus"
description: "Exact source-derived schema reference for schemas/synthetic-corpus.schema.json"
---

# `schemas/synthetic-corpus.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/synthetic-corpus.schema.json` |
| SHA-256 | `3c05d2c0a766021805afdd306d6a08068af6a24cdb0adb82fb3eca4d0f1d7c7d` |
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
| `case_count` | `integer` | yes | Not declared |
| `cases` | `array` | yes | Not declared |
| `cases_per_family` | `integer` | yes | Not declared |
| `created_at` | `string` | yes | Not declared |
| `families` | `array` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `seed` | `integer` | yes | Not declared |
| `truth_scope` | `object` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

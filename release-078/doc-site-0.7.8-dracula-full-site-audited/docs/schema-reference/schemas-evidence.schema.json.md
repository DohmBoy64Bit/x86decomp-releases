---
title: "x86decomp evidence item"
description: "Exact source-derived schema reference for schemas/evidence.schema.json"
---

# `schemas/evidence.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/evidence.schema.json` |
| SHA-256 | `5c5199ae9f480dbbb28eb3ebd889a53a46c08535cabf346d3a0bf04f4a4aa7bd` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:evidence:1` |
| Title | x86decomp evidence item |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `id`
- `kind`
- `source`
- `locator`
- `assertion`
- `independent_group`
- `digest_sha256`
- `observed_at`
- `metadata`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `assertion` | `string` | yes | Not declared |
| `digest_sha256` | `string, null` | yes | Not declared |
| `id` | `string` | yes | Not declared |
| `independent_group` | `string` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `locator` | `string` | yes | Not declared |
| `metadata` | `object` | yes | Not declared |
| `observed_at` | `string` | yes | Not declared |
| `source` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

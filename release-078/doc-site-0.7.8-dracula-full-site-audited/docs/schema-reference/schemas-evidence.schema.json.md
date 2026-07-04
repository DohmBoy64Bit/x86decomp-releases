---
title: "x86decomp evidence item"
description: "Schema reference for schemas/evidence.schema.json"
---

# `schemas/evidence.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/evidence.schema.json` |
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
| `assertion` | `string` | yes | — |
| `digest_sha256` | `string, null` | yes | — |
| `id` | `string` | yes | — |
| `independent_group` | `string` | yes | — |
| `kind` | — | yes | — |
| `locator` | `string` | yes | — |
| `metadata` | `object` | yes | — |
| `observed_at` | `string` | yes | — |
| `source` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


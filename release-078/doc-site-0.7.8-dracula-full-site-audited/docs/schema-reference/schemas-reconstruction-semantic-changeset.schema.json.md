---
title: "Semantic changeset"
description: "Schema reference for schemas/reconstruction/semantic-changeset.schema.json"
---

# `schemas/reconstruction/semantic-changeset.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/semantic-changeset.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/semantic-changeset.schema.json` |
| Title | Semantic changeset |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `changeset_id`
- `name`
- `operations`
- `status`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `base_audit_hash` | `string, null` | no | — |
| `changeset_id` | `string` | yes | — |
| `name` | `string` | yes | — |
| `operations` | `array` | yes | — |
| `status` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


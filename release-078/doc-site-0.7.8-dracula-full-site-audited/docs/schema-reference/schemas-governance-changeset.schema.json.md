---
title: "changeset manifest"
description: "Schema reference for schemas/governance/changeset.schema.json"
---

# `schemas/governance/changeset.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/changeset.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | — |
| Title | changeset manifest |
| Top-level type | `object` |
| Top-level properties | 6 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `format`
- `changeset_id`
- `base_event_hash`
- `tip_event_hash`
- `event_count`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `base_event_hash` | `string, null` | yes | — |
| `changeset_id` | `string` | yes | — |
| `created_at` | `string` | no | — |
| `event_count` | `integer` | yes | — |
| `format` | — | yes | — |
| `tip_event_hash` | `string, null` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "changeset manifest"
description: "Exact source-derived schema reference for schemas/governance/changeset.schema.json"
---

# `schemas/governance/changeset.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/changeset.schema.json` |
| SHA-256 | `6788b90056dbf46cdaaaab292bdc6c3102e20ff47c790f131b47c15d08f5cbd3` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `Not declared` |
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
| `base_event_hash` | `string, null` | yes | Not declared |
| `changeset_id` | `string` | yes | Not declared |
| `created_at` | `string` | no | Not declared |
| `event_count` | `integer` | yes | Not declared |
| `format` | `Not declared` | yes | Not declared |
| `tip_event_hash` | `string, null` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

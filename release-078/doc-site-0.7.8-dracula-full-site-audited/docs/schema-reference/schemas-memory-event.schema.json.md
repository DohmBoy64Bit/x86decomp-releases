---
title: "x86decomp project memory event"
description: "Schema reference for schemas/memory-event.schema.json"
---

# `schemas/memory-event.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/memory-event.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:memory-event:1` |
| Title | x86decomp project memory event |
| Top-level type | `object` |
| Top-level properties | 11 |
| Required fields | 11 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `id`
- `sequence`
- `timestamp`
- `actor`
- `category`
- `summary`
- `details`
- `evidence_ids`
- `previous_hash`
- `event_hash`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `actor` | `string` | yes | — |
| `category` | `string` | yes | — |
| `details` | `object` | yes | — |
| `event_hash` | `string` | yes | — |
| `evidence_ids` | `array` | yes | — |
| `id` | `string` | yes | — |
| `previous_hash` | `string, null` | yes | — |
| `schema_version` | — | yes | — |
| `sequence` | `integer` | yes | — |
| `summary` | `string` | yes | — |
| `timestamp` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


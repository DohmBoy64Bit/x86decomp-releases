---
title: "x86decomp project memory event"
description: "Exact source-derived schema reference for schemas/memory-event.schema.json"
---

# `schemas/memory-event.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/memory-event.schema.json` |
| SHA-256 | `d2f38971ac7dda92dda0564bb77bb4858160b5a342476d36fe52238eb5289e74` |
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
| `actor` | `string` | yes | Not declared |
| `category` | `string` | yes | Not declared |
| `details` | `object` | yes | Not declared |
| `event_hash` | `string` | yes | Not declared |
| `evidence_ids` | `array` | yes | Not declared |
| `id` | `string` | yes | Not declared |
| `previous_hash` | `string, null` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `sequence` | `integer` | yes | Not declared |
| `summary` | `string` | yes | Not declared |
| `timestamp` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

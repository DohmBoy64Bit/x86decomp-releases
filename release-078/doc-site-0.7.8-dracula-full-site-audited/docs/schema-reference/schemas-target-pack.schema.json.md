---
title: "target-pack.schema.json"
description: "Exact source-derived schema reference for schemas/target-pack.schema.json"
---

# `schemas/target-pack.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/target-pack.schema.json` |
| SHA-256 | `867b89f3738ff1310340d078c5ae530f0087277e96cd00106fa1275cd0bcc954` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:target-pack:1` |
| Title | Not declared |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 12 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `target_id`
- `name`
- `created_at`
- `architecture`
- `image_kind`
- `primary_image`
- `primary_sha256`
- `default_modes`
- `scope`
- `decisions`
- `artifacts`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | `Not declared` | yes | Not declared |
| `artifacts` | `array` | yes | Not declared |
| `created_at` | `string` | yes | Not declared |
| `decisions` | `object` | yes | Not declared |
| `default_modes` | `Not declared` | yes | Not declared |
| `image_kind` | `Not declared` | yes | Not declared |
| `name` | `string` | yes | Not declared |
| `primary_image` | `string` | yes | Not declared |
| `primary_sha256` | `string` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `scope` | `object` | yes | Not declared |
| `target_id` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

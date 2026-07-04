---
title: "Type/ABI constraint record"
description: "Schema reference for schemas/type-constraint.schema.json"
---

# `schemas/type-constraint.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/type-constraint.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:type-constraint:1` |
| Title | Type/ABI constraint record |
| Top-level type | `object` |
| Top-level properties | 8 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `subject_entity`
- `relation`
- `object_value`
- `provenance`
- `status`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `confidence` | `number, null` | no | — |
| `constraint_id` | `integer` | no | — |
| `evidence_id` | `string, null` | no | — |
| `object_value` | `string` | yes | — |
| `provenance` | `string` | yes | — |
| `relation` | `string` | yes | — |
| `status` | — | yes | — |
| `subject_entity` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


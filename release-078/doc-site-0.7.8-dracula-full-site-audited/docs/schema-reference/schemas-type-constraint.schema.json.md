---
title: "Type/ABI constraint record"
description: "Exact source-derived schema reference for schemas/type-constraint.schema.json"
---

# `schemas/type-constraint.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/type-constraint.schema.json` |
| SHA-256 | `f98328b457deccc685ea8be764507320d5ff94deddb366e47c5018a678baa59d` |
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
| `confidence` | `number, null` | no | Not declared |
| `constraint_id` | `integer` | no | Not declared |
| `evidence_id` | `string, null` | no | Not declared |
| `object_value` | `string` | yes | Not declared |
| `provenance` | `string` | yes | Not declared |
| `relation` | `string` | yes | Not declared |
| `status` | `Not declared` | yes | Not declared |
| `subject_entity` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

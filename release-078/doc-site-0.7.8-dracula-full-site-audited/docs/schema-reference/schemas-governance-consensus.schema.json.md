---
title: "consensus observation"
description: "Exact source-derived schema reference for schemas/governance/consensus.schema.json"
---

# `schemas/governance/consensus.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/consensus.schema.json` |
| SHA-256 | `f3edcf4a5962701cde7a0f4f483a19d49e9f5beea5e6a4dc3c643c9970ee9c43` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `Not declared` |
| Title | consensus observation |
| Top-level type | `object` |
| Top-level properties | 9 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `subject_kind`
- `subject_id`
- `property_name`
- `value`
- `adapter_name`
- `adapter_version`
- `evidence_id`
- `independence_group`
- `confidence`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `adapter_name` | `string` | yes | Not declared |
| `adapter_version` | `string` | yes | Not declared |
| `confidence` | `number` | yes | Not declared |
| `evidence_id` | `string` | yes | Not declared |
| `independence_group` | `string` | yes | Not declared |
| `property_name` | `string` | yes | Not declared |
| `subject_id` | `string` | yes | Not declared |
| `subject_kind` | `string` | yes | Not declared |
| `value` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

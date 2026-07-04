---
title: "consensus observation"
description: "Schema reference for schemas/governance/consensus.schema.json"
---

# `schemas/governance/consensus.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/consensus.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | — |
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
| `adapter_name` | `string` | yes | — |
| `adapter_version` | `string` | yes | — |
| `confidence` | `number` | yes | — |
| `evidence_id` | `string` | yes | — |
| `independence_group` | `string` | yes | — |
| `property_name` | `string` | yes | — |
| `subject_id` | `string` | yes | — |
| `subject_kind` | `string` | yes | — |
| `value` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


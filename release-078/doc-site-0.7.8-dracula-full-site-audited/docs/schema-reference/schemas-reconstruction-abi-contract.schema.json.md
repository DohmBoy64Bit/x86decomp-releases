---
title: "ABI contract"
description: "Schema reference for schemas/reconstruction/abi-contract.schema.json"
---

# `schemas/reconstruction/abi-contract.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/abi-contract.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/abi-contract.schema.json` |
| Title | ABI contract |
| Top-level type | `object` |
| Top-level properties | 6 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `contract_id`
- `subject_kind`
- `subject_id`
- `architecture`
- `contract`
- `evidence`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `contract` | `object` | yes | — |
| `contract_id` | `string` | yes | — |
| `evidence` | `array` | yes | — |
| `subject_id` | `string` | yes | — |
| `subject_kind` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


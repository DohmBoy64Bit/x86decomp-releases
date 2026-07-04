---
title: "counterexample"
description: "Schema reference for schemas/governance/counterexample.schema.json"
---

# `schemas/governance/counterexample.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/counterexample.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | — |
| Title | counterexample |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `scope_kind`
- `scope_id`
- `current_sha256`
- `size_bytes`
- `state`
- `predicate`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `current_sha256` | `string` | yes | — |
| `predicate` | `object` | yes | — |
| `provenance` | `object` | no | — |
| `scope_id` | `string` | yes | — |
| `scope_kind` | `string` | yes | — |
| `size_bytes` | `integer` | yes | — |
| `state` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


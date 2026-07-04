---
title: "hypothesis"
description: "Schema reference for schemas/governance/hypothesis.schema.json"
---

# `schemas/governance/hypothesis.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/hypothesis.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | — |
| Title | hypothesis |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `statement`
- `scope_kind`
- `scope_id`
- `state`
- `confidence`
- `origin`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `confidence` | `number` | yes | — |
| `locked` | `boolean` | no | — |
| `origin` | `string` | yes | — |
| `scope_id` | `string` | yes | — |
| `scope_kind` | `string` | yes | — |
| `state` | — | yes | — |
| `statement` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


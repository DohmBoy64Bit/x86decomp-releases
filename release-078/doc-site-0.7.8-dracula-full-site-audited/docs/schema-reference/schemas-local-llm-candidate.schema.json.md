---
title: "Local LLM C proposal response"
description: "Schema reference for schemas/local-llm/candidate.schema.json"
---

# `schemas/local-llm/candidate.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/local-llm/candidate.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.local/schemas/local-llm/candidate.schema.json` |
| Title | Local LLM C proposal response |
| Top-level type | `object` |
| Top-level properties | 4 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `status`
- `c_source`
- `assumptions`
- `rationale`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `assumptions` | `array` | yes | — |
| `c_source` | `string` | yes | — |
| `rationale` | `string` | yes | — |
| `status` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "Integration scenario manifest"
description: "Schema reference for schemas/integration-scenarios.schema.json"
---

# `schemas/integration-scenarios.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/integration-scenarios.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:integration-scenarios:1` |
| Title | Integration scenario manifest |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 4 |
| Definitions / `$defs` | 1 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `name`
- `execution`
- `scenarios`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `captured_output_limit` | `integer` | no | — |
| `execution` | `object` | yes | — |
| `name` | `string` | yes | — |
| `scenarios` | `array` | yes | — |
| `schema_version` | — | yes | — |

## Definition keys

- `process`

## Source verification


---
title: "worker profile"
description: "Schema reference for schemas/governance/worker.schema.json"
---

# `schemas/governance/worker.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/governance/worker.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | — |
| Title | worker profile |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 3 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `name`
- `status`
- `capabilities`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `capabilities` | `object` | yes | — |
| `endpoint` | `string, null` | no | — |
| `environment_sha256` | `string, null` | no | — |
| `name` | `string` | yes | — |
| `status` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


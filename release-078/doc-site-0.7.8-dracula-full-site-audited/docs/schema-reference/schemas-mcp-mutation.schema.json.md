---
title: "Evidence-gated MCP mutation"
description: "Schema reference for schemas/mcp-mutation.schema.json"
---

# `schemas/mcp-mutation.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/mcp-mutation.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:mcp-mutation:1` |
| Title | Evidence-gated MCP mutation |
| Top-level type | `object` |
| Top-level properties | 10 |
| Required fields | 8 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `created_at`
- `tool`
- `arguments`
- `rationale`
- `evidence_ids`
- `status`
- `approval_hash`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `approval_hash` | `string` | yes | — |
| `arguments` | `object` | yes | — |
| `committed_at` | `string` | no | — |
| `created_at` | `string` | yes | — |
| `evidence_ids` | `array` | yes | — |
| `rationale` | `string` | yes | — |
| `result` | `object` | no | — |
| `schema_version` | — | yes | — |
| `status` | — | yes | — |
| `tool` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


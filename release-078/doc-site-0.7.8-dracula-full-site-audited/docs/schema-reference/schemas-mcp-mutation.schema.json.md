---
title: "Evidence-gated MCP mutation"
description: "Exact source-derived schema reference for schemas/mcp-mutation.schema.json"
---

# `schemas/mcp-mutation.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/mcp-mutation.schema.json` |
| SHA-256 | `64335798160269133e880d823f14de7f0cb4f2dafbf0c47526e24fb9fb16ea29` |
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
| `approval_hash` | `string` | yes | Not declared |
| `arguments` | `object` | yes | Not declared |
| `committed_at` | `string` | no | Not declared |
| `created_at` | `string` | yes | Not declared |
| `evidence_ids` | `array` | yes | Not declared |
| `rationale` | `string` | yes | Not declared |
| `result` | `object` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `status` | `Not declared` | yes | Not declared |
| `tool` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

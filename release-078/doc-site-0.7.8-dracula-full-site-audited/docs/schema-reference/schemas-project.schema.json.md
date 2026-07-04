---
title: "x86decomp project (schema versions 1, 2, and 3)"
description: "Schema reference for schemas/project.schema.json"
---

# `schemas/project.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/project.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:project:3` |
| Title | x86decomp project (schema versions 1, 2, and 3) |
| Top-level type | `object` |
| Top-level properties | 21 |
| Required fields | 10 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `project_id`
- `created_at`
- `supported_scope`
- `binary`
- `program_manifest`
- `memory_ledger`
- `function_root`
- `evidence_root`
- `status`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_database` | `string` | no | — |
| `architecture` | — | no | — |
| `binary` | `object` | yes | — |
| `content_store` | `string` | no | — |
| `created_at` | `string` | yes | — |
| `default_modes` | — | no | — |
| `evidence_root` | `string` | yes | — |
| `function_root` | `string` | yes | — |
| `memory_ledger` | `string` | yes | — |
| `orchestration_root` | `string` | no | — |
| `program_manifest` | `string` | yes | — |
| `project_id` | `string` | yes | — |
| `project_state_database` | `string` | no | — |
| `schema_version` | — | yes | — |
| `status` | — | yes | — |
| `supported_scope` | — | yes | — |
| `target_id` | `string` | no | — |
| `target_pack` | `string` | no | — |
| `template_kind` | — | no | — |
| `toolkit_release` | `string` | no | — |
| `work_queue` | `string` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


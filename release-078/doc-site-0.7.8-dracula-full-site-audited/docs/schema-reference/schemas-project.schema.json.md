---
title: "x86decomp project (schema versions 1, 2, and 3)"
description: "Exact source-derived schema reference for schemas/project.schema.json"
---

# `schemas/project.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/project.schema.json` |
| SHA-256 | `4ab19d9064e8d249fdd545d1fa183920902d6afbe647d004ddd571a208295b0b` |
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
| `analysis_database` | `string` | no | Not declared |
| `architecture` | `Not declared` | no | Not declared |
| `binary` | `object` | yes | Not declared |
| `content_store` | `string` | no | Not declared |
| `created_at` | `string` | yes | Not declared |
| `default_modes` | `Not declared` | no | Not declared |
| `evidence_root` | `string` | yes | Not declared |
| `function_root` | `string` | yes | Not declared |
| `memory_ledger` | `string` | yes | Not declared |
| `orchestration_root` | `string` | no | Not declared |
| `program_manifest` | `string` | yes | Not declared |
| `project_id` | `string` | yes | Not declared |
| `project_state_database` | `string` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `status` | `Not declared` | yes | Not declared |
| `supported_scope` | `Not declared` | yes | Not declared |
| `target_id` | `string` | no | Not declared |
| `target_pack` | `string` | no | Not declared |
| `template_kind` | `Not declared` | no | Not declared |
| `toolkit_release` | `string` | no | Not declared |
| `work_queue` | `string` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

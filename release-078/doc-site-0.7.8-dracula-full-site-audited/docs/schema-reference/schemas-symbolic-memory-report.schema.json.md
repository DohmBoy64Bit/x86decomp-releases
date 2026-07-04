---
title: "Bounded angr symbolic memory-alias comparison"
description: "Schema reference for schemas/symbolic-memory-report.schema.json"
---

# `schemas/symbolic-memory-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/symbolic-memory-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:symbolic-memory-report:1` |
| Title | Bounded angr symbolic memory-alias comparison |
| Top-level type | `object` |
| Top-level properties | 11 |
| Required fields | 9 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `architecture`
- `harness`
- `target_execution`
- `candidate_execution`
- `equivalent_within_completed_model`
- `scope_statement`
- `universal_equivalence_claimed`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | — | yes | — |
| `candidate_execution` | `object` | yes | — |
| `candidate_sha256` | `string` | no | — |
| `equivalent_within_completed_model` | `boolean` | yes | — |
| `harness` | `object` | yes | — |
| `kind` | — | yes | — |
| `schema_version` | — | yes | — |
| `scope_statement` | `string` | yes | — |
| `target_execution` | `object` | yes | — |
| `target_sha256` | `string` | no | — |
| `universal_equivalence_claimed` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "Bounded angr symbolic memory-alias comparison"
description: "Exact source-derived schema reference for schemas/symbolic-memory-report.schema.json"
---

# `schemas/symbolic-memory-report.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/symbolic-memory-report.schema.json` |
| SHA-256 | `5e17dedb1bedf6581662f4cced118e40b8075957a161daea2abfab778d0298ba` |
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
| `architecture` | `Not declared` | yes | Not declared |
| `candidate_execution` | `object` | yes | Not declared |
| `candidate_sha256` | `string` | no | Not declared |
| `equivalent_within_completed_model` | `boolean` | yes | Not declared |
| `harness` | `object` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `scope_statement` | `string` | yes | Not declared |
| `target_execution` | `object` | yes | Not declared |
| `target_sha256` | `string` | no | Not declared |
| `universal_equivalence_claimed` | `Not declared` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

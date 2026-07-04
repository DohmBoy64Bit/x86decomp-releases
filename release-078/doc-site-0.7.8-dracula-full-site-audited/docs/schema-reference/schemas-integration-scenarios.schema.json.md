---
title: "Integration scenario manifest"
description: "Exact source-derived schema reference for schemas/integration-scenarios.schema.json"
---

# `schemas/integration-scenarios.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/integration-scenarios.schema.json` |
| SHA-256 | `60799068b8df90e7d457415f6e08fa236a0620630ddab2641dec2ff8bac6e43e` |
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
| `captured_output_limit` | `integer` | no | Not declared |
| `execution` | `object` | yes | Not declared |
| `name` | `string` | yes | Not declared |
| `scenarios` | `array` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |

## Definition keys

- `process`

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

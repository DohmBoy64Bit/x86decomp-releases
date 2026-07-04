---
title: "objdiff external invocation manifest"
description: "Exact source-derived schema reference for schemas/objdiff-manifest.schema.json"
---

# `schemas/objdiff-manifest.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/objdiff-manifest.schema.json` |
| SHA-256 | `2fe8f65399749687b2890cc643f474c0b8de221e90f6ae5013ce0d8b46590360` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:objdiff-manifest:1` |
| Title | objdiff external invocation manifest |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 4 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `target`
- `candidate`
- `arguments`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `arguments` | `array` | yes | Not declared |
| `candidate` | `string` | yes | Not declared |
| `environment` | `object` | no | Not declared |
| `executable` | `string` | no | Not declared |
| `inherit_environment` | `boolean` | no | Not declared |
| `output` | `string` | no | Not declared |
| `output_format` | `Not declared` | no | Not declared |
| `require_output` | `boolean` | no | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `success_exit_codes` | `array` | no | Not declared |
| `target` | `string` | yes | Not declared |
| `timeout_seconds` | `integer` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

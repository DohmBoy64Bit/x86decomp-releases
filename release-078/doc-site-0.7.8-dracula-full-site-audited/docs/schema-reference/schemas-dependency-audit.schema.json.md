---
title: "x86decomp dependency vulnerability audit"
description: "Exact source-derived schema reference for schemas/dependency-audit.schema.json"
---

# `schemas/dependency-audit.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/dependency-audit.schema.json` |
| SHA-256 | `2eef4097789050d846536b406ccd7b9e8e639467bdf1ca530045fcc6050c8ee2` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:dependency-audit:1` |
| Title | x86decomp dependency vulnerability audit |
| Top-level type | `object` |
| Top-level properties | 12 |
| Required fields | 11 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `kind`
- `created_at`
- `tool`
- `tool_sha256`
- `return_code`
- `dependency_count`
- `vulnerability_count`
- `vulnerabilities`
- `passed`
- `raw_report`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `created_at` | `string` | yes | Not declared |
| `dependency_count` | `integer` | yes | Not declared |
| `kind` | `Not declared` | yes | Not declared |
| `passed` | `boolean` | yes | Not declared |
| `raw_report` | `Not declared` | yes | Not declared |
| `return_code` | `integer` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `stderr` | `string` | no | Not declared |
| `tool` | `string` | yes | Not declared |
| `tool_sha256` | `string` | yes | Not declared |
| `vulnerabilities` | `array` | yes | Not declared |
| `vulnerability_count` | `integer` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

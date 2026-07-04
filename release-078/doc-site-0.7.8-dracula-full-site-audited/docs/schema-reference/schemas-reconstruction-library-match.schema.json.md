---
title: "Static library recognition candidate"
description: "Exact source-derived schema reference for schemas/reconstruction/library-match.schema.json"
---

# `schemas/reconstruction/library-match.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/library-match.schema.json` |
| SHA-256 | `cdf8967118c99e0f1d224829f1e3067a2b9db50f31ca945db68a3cec61b0f36e` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/library-match.schema.json` |
| Title | Static library recognition candidate |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 6 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `match_id`
- `subject_id`
- `library_name`
- `confidence`
- `evidence`
- `disposition`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `confidence` | `number` | yes | Not declared |
| `disposition` | `Not declared` | yes | Not declared |
| `evidence` | `array` | yes | Not declared |
| `library_name` | `string` | yes | Not declared |
| `match_id` | `string` | yes | Not declared |
| `subject_id` | `string` | yes | Not declared |
| `version_range` | `string, null` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

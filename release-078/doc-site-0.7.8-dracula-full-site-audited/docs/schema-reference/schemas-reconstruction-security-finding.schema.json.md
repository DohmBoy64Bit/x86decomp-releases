---
title: "Security finding"
description: "Exact source-derived schema reference for schemas/reconstruction/security-finding.schema.json"
---

# `schemas/reconstruction/security-finding.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/security-finding.schema.json` |
| SHA-256 | `9a4f8a220e2e2d1d7dbc8116968bf2752d57a5725e18673faf59a192ace1826e` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `https://x86decomp.dev/schemas/reconstruction/security-finding.schema.json` |
| Title | Security finding |
| Top-level type | `object` |
| Top-level properties | 7 |
| Required fields | 7 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `finding_id`
- `rule_id`
- `severity`
- `subject_id`
- `summary`
- `evidence`
- `status`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `evidence` | `array` | yes | Not declared |
| `finding_id` | `string` | yes | Not declared |
| `rule_id` | `string` | yes | Not declared |
| `severity` | `Not declared` | yes | Not declared |
| `status` | `string` | yes | Not declared |
| `subject_id` | `string` | yes | Not declared |
| `summary` | `string` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

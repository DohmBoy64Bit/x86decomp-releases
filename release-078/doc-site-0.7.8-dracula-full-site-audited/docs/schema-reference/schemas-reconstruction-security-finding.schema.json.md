---
title: "Security finding"
description: "Schema reference for schemas/reconstruction/security-finding.schema.json"
---

# `schemas/reconstruction/security-finding.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/reconstruction/security-finding.schema.json` |
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
| `evidence` | `array` | yes | — |
| `finding_id` | `string` | yes | — |
| `rule_id` | `string` | yes | — |
| `severity` | — | yes | — |
| `status` | `string` | yes | — |
| `subject_id` | `string` | yes | — |
| `summary` | `string` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


---
title: "x86decomp Authorized Static Test Bundle"
description: "Schema reference for schemas/test-bundle.schema.json"
---

# `schemas/test-bundle.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/test-bundle.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:test-bundle:1` |
| Title | x86decomp Authorized Static Test Bundle |
| Top-level type | `object` |
| Top-level properties | 6 |
| Required fields | 3 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `authorization`
- `artifacts`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `artifacts` | `array` | yes | — |
| `authorization` | `object` | yes | — |
| `description` | `string` | no | — |
| `expected_architecture` | — | no | — |
| `name` | `string` | no | — |
| `schema_version` | — | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


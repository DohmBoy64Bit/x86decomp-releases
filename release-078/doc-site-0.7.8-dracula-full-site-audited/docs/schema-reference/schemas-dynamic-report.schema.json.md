---
title: "Bounded Unicorn differential report"
description: "Schema reference for schemas/dynamic-report.schema.json"
---

# `schemas/dynamic-report.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/dynamic-report.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:dynamic-report:1` |
| Title | Bounded Unicorn differential report |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `true` |

## Required fields

- `schema_version`
- `equivalent_for_harness`
- `target`
- `candidate`
- `scope_statement`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate` | `object` | yes | — |
| `equivalent_for_harness` | `boolean` | yes | — |
| `schema_version` | — | yes | — |
| `scope_statement` | `string` | yes | — |
| `target` | `object` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


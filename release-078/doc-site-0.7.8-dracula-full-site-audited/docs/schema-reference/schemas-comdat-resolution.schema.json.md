---
title: "COFF COMDAT resolution report"
description: "Schema reference for schemas/comdat-resolution.schema.json"
---

# `schemas/comdat-resolution.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/comdat-resolution.schema.json` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:comdat-resolution:1` |
| Title | COFF COMDAT resolution report |
| Top-level type | `object` |
| Top-level properties | 5 |
| Required fields | 5 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `schema_version`
- `valid`
- `winners`
- `discarded`
- `conflicts`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `conflicts` | `array` | yes | — |
| `discarded` | `array` | yes | — |
| `schema_version` | — | yes | — |
| `valid` | `boolean` | yes | — |
| `winners` | `array` | yes | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


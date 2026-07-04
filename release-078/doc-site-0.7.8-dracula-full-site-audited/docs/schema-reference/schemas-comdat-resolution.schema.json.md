---
title: "COFF COMDAT resolution report"
description: "Exact source-derived schema reference for schemas/comdat-resolution.schema.json"
---

# `schemas/comdat-resolution.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/comdat-resolution.schema.json` |
| SHA-256 | `01fd177dfa983202ca8770e7985aa623e166fd22c20fdecc1d3d37f9cbfe0aae` |
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
| `conflicts` | `array` | yes | Not declared |
| `discarded` | `array` | yes | Not declared |
| `schema_version` | `Not declared` | yes | Not declared |
| `valid` | `boolean` | yes | Not declared |
| `winners` | `array` | yes | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

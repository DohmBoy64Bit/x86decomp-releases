---
title: "x86decomp ABI contract"
description: "Exact source-derived schema reference for schemas/abi-contract.schema.json"
---

# `schemas/abi-contract.schema.json`

This page is generated from the exact schema file in the v0.7.8 source tree. It is not an inferred or hand-written summary.

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/abi-contract.schema.json` |
| SHA-256 | `536e89f5ab760329f3799138b17c8a321170fc1fc729528d97b7f75d4af96c76` |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `urn:x86decomp:schema:abi-contract:1` |
| Title | x86decomp ABI contract |
| Top-level type | `object` |
| Top-level properties | 10 |
| Required fields | 2 |
| Definitions / `$defs` | 0 |
| `additionalProperties` | `false` |

## Required fields

- `architecture`
- `convention`

## Top-level properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `architecture` | `Not declared` | yes | Not declared |
| `callee_stack_cleanup` | `integer, null` | no | Not declared |
| `convention` | `Not declared` | yes | Not declared |
| `floating_point` | `Not declared` | no | Not declared |
| `register_arguments` | `array` | no | Not declared |
| `return_registers` | `array` | no | Not declared |
| `stack_argument_bytes` | `integer, null` | no | Not declared |
| `structure_return` | `boolean` | no | Not declared |
| `this_register` | `string, null` | no | Not declared |
| `variadic` | `boolean` | no | Not declared |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification

The schema audit verifies that this page names the same source path and SHA-256 hash as the file in the v0.7.8 toolkit archive, and that the source schema passes JSON Schema meta-validation.

---
title: "x86decomp ABI contract"
description: "Schema reference for schemas/abi-contract.schema.json"
---

# `schemas/abi-contract.schema.json`

| Field | Value |
| --- | --- |
| Scope | `toolkit` |
| Source path | `schemas/abi-contract.schema.json` |
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
| `architecture` | — | yes | — |
| `callee_stack_cleanup` | `integer, null` | no | — |
| `convention` | — | yes | — |
| `floating_point` | — | no | — |
| `register_arguments` | `array` | no | — |
| `return_registers` | `array` | no | — |
| `stack_argument_bytes` | `integer, null` | no | — |
| `structure_return` | `boolean` | no | — |
| `this_register` | `string, null` | no | — |
| `variadic` | `boolean` | no | — |

## Definition keys

This schema declares no top-level `definitions` or `$defs` object.

## Source verification


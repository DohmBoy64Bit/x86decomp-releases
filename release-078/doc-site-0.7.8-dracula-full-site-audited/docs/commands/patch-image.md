---
title: x86decomp patch-image
description: Exact v0.7.8 parser-derived reference for `x86decomp patch-image`.
---


# `x86decomp patch-image`

## Usage

```text
usage: x86decomp patch-image [-h] --rva RVA
                             [--expected-original-sha256 EXPECTED_ORIGINAL_SHA256]
                             [--expected-function-sha256 EXPECTED_FUNCTION_SHA256]
                             [--report REPORT]
                             original candidate output
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required · type: `_path` · parser destination: `original`. No help text declared. |
| `candidate` | required · type: `_path` · parser destination: `candidate`. No help text declared. |
| `output` | required · type: `_path` · parser destination: `output`. No help text declared. |
| `--rva` | required · type: `_int` · parser destination: `rva`. No help text declared. |
| `--expected-original-sha256` | parser destination: `expected_original_sha256`. No help text declared. |
| `--expected-function-sha256` | parser destination: `expected_function_sha256`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

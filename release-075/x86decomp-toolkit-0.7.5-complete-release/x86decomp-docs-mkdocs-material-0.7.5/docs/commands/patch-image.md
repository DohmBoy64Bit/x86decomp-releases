---
title: x86decomp patch-image
description: Exact parser-derived reference for x86decomp patch-image in 0.7.5.
---

# `x86decomp patch-image`

## `x86decomp patch-image`

usage: x86decomp patch-image [-h] --rva RVA

### Usage

```text
x86decomp patch-image [-h] --rva RVA
                             [--expected-original-sha256 EXPECTED_ORIGINAL_SHA256]
                             [--expected-function-sha256 EXPECTED_FUNCTION_SHA256]
                             [--report REPORT]
                             original candidate output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required · type: `_path`. No help text is declared; parser destination is `original`. |
| `candidate` | required · type: `_path`. No help text is declared; parser destination is `candidate`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--rva` | required · type: `_int`. No help text is declared; parser destination is `rva`. |
| `--expected-original-sha256` | declared. No help text is declared; parser destination is `expected_original_sha256`. |
| `--expected-function-sha256` | declared. No help text is declared; parser destination is `expected_function_sha256`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

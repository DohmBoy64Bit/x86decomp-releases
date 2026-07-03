---
title: x86decomp coff-extract
description: Exact parser-derived reference for x86decomp coff-extract in 0.7.5.
---

# `x86decomp coff-extract`

## `x86decomp coff-extract`

usage: x86decomp coff-extract [-h] [--size SIZE] object symbol output

### Usage

```text
x86decomp coff-extract [-h] [--size SIZE] object symbol output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `object` | required · type: `_path`. No help text is declared; parser destination is `object`. |
| `symbol` | required. No help text is declared; parser destination is `symbol`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--size` | type: `_int`. No help text is declared; parser destination is `size`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

---
title: x86decomp diff-function
description: Exact parser-derived reference for x86decomp diff-function in 0.7.5.
---

# `x86decomp diff-function`

## `x86decomp diff-function`

usage: x86decomp diff-function [-h] [--report REPORT] pe rva size coff symbol

### Usage

```text
x86decomp diff-function [-h] [--report REPORT] pe rva size coff symbol
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path`. No help text is declared; parser destination is `pe`. |
| `rva` | required · type: `_int`. No help text is declared; parser destination is `rva`. |
| `size` | required · type: `_int`. No help text is declared; parser destination is `size`. |
| `coff` | required · type: `_path`. No help text is declared; parser destination is `coff`. |
| `symbol` | required. No help text is declared; parser destination is `symbol`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

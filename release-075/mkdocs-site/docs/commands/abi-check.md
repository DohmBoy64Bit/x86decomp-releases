---
title: x86decomp abi-check
description: Exact parser-derived reference for x86decomp abi-check in 0.7.5.
---

# `x86decomp abi-check`

## `x86decomp abi-check`

usage: x86decomp abi-check [-h] [--base BASE] [--report REPORT] code contract

### Usage

```text
x86decomp abi-check [-h] [--base BASE] [--report REPORT] code contract
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `code` | required · type: `_path`. No help text is declared; parser destination is `code`. |
| `contract` | required · type: `_path`. No help text is declared; parser destination is `contract`. |
| `--base` | default: `0` · type: `_int`. No help text is declared; parser destination is `base`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

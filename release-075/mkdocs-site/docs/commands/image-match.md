---
title: x86decomp image-match
description: Exact parser-derived reference for x86decomp image-match in 0.7.5.
---

# `x86decomp image-match`

## `x86decomp image-match`

usage: x86decomp image-match [-h] [--profile PROFILE] [--report REPORT]

### Usage

```text
x86decomp image-match [-h] [--profile PROFILE] [--report REPORT]
                             reference candidate
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `reference` | required · type: `_path`. No help text is declared; parser destination is `reference`. |
| `candidate` | required · type: `_path`. No help text is declared; parser destination is `candidate`. |
| `--profile` | type: `_path`. No help text is declared; parser destination is `profile`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

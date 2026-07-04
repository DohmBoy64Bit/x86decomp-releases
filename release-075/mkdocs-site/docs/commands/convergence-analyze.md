---
title: x86decomp convergence-analyze
description: Exact parser-derived reference for x86decomp convergence-analyze in 0.7.5.
---

# `x86decomp convergence-analyze`

## `x86decomp convergence-analyze`

usage: x86decomp convergence-analyze [-h] [--profile PROFILE]

### Usage

```text
x86decomp convergence-analyze [-h] [--profile PROFILE]
                                     [--previous PREVIOUS] [--report REPORT]
                                     [--history HISTORY]
                                     reference candidate
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `reference` | required · type: `_path`. No help text is declared; parser destination is `reference`. |
| `candidate` | required · type: `_path`. No help text is declared; parser destination is `candidate`. |
| `--profile` | type: `_path`. No help text is declared; parser destination is `profile`. |
| `--previous` | type: `_path`. No help text is declared; parser destination is `previous`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |
| `--history` | type: `_path`. No help text is declared; parser destination is `history`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

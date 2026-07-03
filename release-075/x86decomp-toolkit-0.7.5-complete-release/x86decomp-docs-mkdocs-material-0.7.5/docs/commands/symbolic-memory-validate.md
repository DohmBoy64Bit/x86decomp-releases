---
title: x86decomp symbolic-memory-validate
description: Exact parser-derived reference for x86decomp symbolic-memory-validate
  in 0.7.5.
---

# `x86decomp symbolic-memory-validate`

## `x86decomp symbolic-memory-validate`

usage: x86decomp symbolic-memory-validate [-h] [--report REPORT]

### Usage

```text
x86decomp symbolic-memory-validate [-h] [--report REPORT]
                                          target candidate harness
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target` | required · type: `_path`. No help text is declared; parser destination is `target`. |
| `candidate` | required · type: `_path`. No help text is declared; parser destination is `candidate`. |
| `harness` | required · type: `_path`. No help text is declared; parser destination is `harness`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

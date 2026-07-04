---
title: x86decomp dependency-audit
description: Exact parser-derived reference for x86decomp dependency-audit in 0.7.5.
---

# `x86decomp dependency-audit`

## `x86decomp dependency-audit`

usage: x86decomp dependency-audit [-h] [--executable EXECUTABLE]

### Usage

```text
x86decomp dependency-audit [-h] [--executable EXECUTABLE]
                                  [--timeout TIMEOUT] [--report REPORT]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--executable` | default: `'pip-audit'`. No help text is declared; parser destination is `executable`. |
| `--timeout` | default: `300` · type: `int`. No help text is declared; parser destination is `timeout`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

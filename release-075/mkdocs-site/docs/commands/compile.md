---
title: x86decomp compile
description: Exact parser-derived reference for x86decomp compile in 0.7.5.
---

# `x86decomp compile`

## `x86decomp compile`

usage: x86decomp compile [-h] [--report REPORT] [--extra-arg EXTRA_ARG]

### Usage

```text
x86decomp compile [-h] [--report REPORT] [--extra-arg EXTRA_ARG]
                         [--cache CACHE]
                         profile source output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · type: `_path`. No help text is declared; parser destination is `profile`. |
| `source` | required · type: `_path`. No help text is declared; parser destination is `source`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |
| `--extra-arg` | default: `[]`. No help text is declared; parser destination is `extra_arg`. |
| `--cache` | type: `_path`. No help text is declared; parser destination is `cache`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

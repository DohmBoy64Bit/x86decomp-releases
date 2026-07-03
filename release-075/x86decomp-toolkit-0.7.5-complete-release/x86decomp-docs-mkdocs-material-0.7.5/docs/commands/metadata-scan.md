---
title: x86decomp metadata-scan
description: Exact parser-derived reference for x86decomp metadata-scan in 0.7.5.
---

# `x86decomp metadata-scan`

## `x86decomp metadata-scan`

usage: x86decomp metadata-scan [-h] [--object OBJECT] [--map MAP]

### Usage

```text
x86decomp metadata-scan [-h] [--object OBJECT] [--map MAP]
                               [--report REPORT]
                               pe
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path`. No help text is declared; parser destination is `pe`. |
| `--object` | default: `[]` · type: `_path`. No help text is declared; parser destination is `object`. |
| `--map` | type: `_path`. No help text is declared; parser destination is `map`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

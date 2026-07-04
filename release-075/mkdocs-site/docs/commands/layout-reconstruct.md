---
title: x86decomp layout-reconstruct
description: Exact parser-derived reference for x86decomp layout-reconstruct in 0.7.5.
---

# `x86decomp layout-reconstruct`

## `x86decomp layout-reconstruct`

usage: x86decomp layout-reconstruct [-h] [--report REPORT]

### Usage

```text
x86decomp layout-reconstruct [-h] [--report REPORT]
                                    pe map [objects ...]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path`. No help text is declared; parser destination is `pe`. |
| `map` | required · type: `_path`. No help text is declared; parser destination is `map`. |
| `objects` | optional · type: `_path` · nargs: `*`. No help text is declared; parser destination is `objects`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

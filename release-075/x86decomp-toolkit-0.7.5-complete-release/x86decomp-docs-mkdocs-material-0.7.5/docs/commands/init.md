---
title: x86decomp init
description: Exact parser-derived reference for x86decomp init in 0.7.5.
---

# `x86decomp init`

## `x86decomp init`

usage: x86decomp init [-h] [--reference-binary] binary project

### Usage

```text
x86decomp init [-h] [--reference-binary] binary project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `binary` | required · type: `_path`. No help text is declared; parser destination is `binary`. |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--reference-binary` | default: `False` · nargs: `0`. No help text is declared; parser destination is `reference_binary`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

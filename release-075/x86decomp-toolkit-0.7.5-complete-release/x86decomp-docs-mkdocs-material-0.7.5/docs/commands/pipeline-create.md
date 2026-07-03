---
title: x86decomp pipeline-create
description: Exact parser-derived reference for x86decomp pipeline-create in 0.7.5.
---

# `x86decomp pipeline-create`

## `x86decomp pipeline-create`

usage: x86decomp pipeline-create [-h] [--without-ghidra] project output

### Usage

```text
x86decomp pipeline-create [-h] [--without-ghidra] project output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--without-ghidra` | default: `False` · nargs: `0`. No help text is declared; parser destination is `without_ghidra`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

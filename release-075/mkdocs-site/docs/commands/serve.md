---
title: x86decomp serve
description: Exact parser-derived reference for x86decomp serve in 0.7.5.
---

# `x86decomp serve`

## `x86decomp serve`

usage: x86decomp serve [-h] [--host HOST] [--port PORT] project

### Usage

```text
x86decomp serve [-h] [--host HOST] [--port PORT] project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--host` | default: `'127.0.0.1'`. No help text is declared; parser destination is `host`. |
| `--port` | default: `8765` · type: `int`. No help text is declared; parser destination is `port`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

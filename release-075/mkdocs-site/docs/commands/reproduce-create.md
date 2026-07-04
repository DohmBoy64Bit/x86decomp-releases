---
title: x86decomp reproduce-create
description: Exact parser-derived reference for x86decomp reproduce-create in 0.7.5.
---

# `x86decomp reproduce-create`

## `x86decomp reproduce-create`

usage: x86decomp reproduce-create [-h] [--required-tool REQUIRED_TOOL]

### Usage

```text
x86decomp reproduce-create [-h] [--required-tool REQUIRED_TOOL]
                                  project output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--required-tool` | declared. No help text is declared; parser destination is `required_tool`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

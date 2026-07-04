---
title: x86decomp work-create
description: Exact parser-derived reference for x86decomp work-create in 0.7.5.
---

# `x86decomp work-create`

## `x86decomp work-create`

usage: x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY]

### Usage

```text
x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY]
                             database function_id {matching,functional} kind
                             instructions
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `function_id` | required. No help text is declared; parser destination is `function_id`. |
| `mode` | required · choices: `matching`, `functional`. No help text is declared; parser destination is `mode`. |
| `kind` | required. No help text is declared; parser destination is `kind`. |
| `instructions` | required. No help text is declared; parser destination is `instructions`. |
| `--validator` | required. No help text is declared; parser destination is `validator`. |
| `--priority` | default: `0` · type: `int`. No help text is declared; parser destination is `priority`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

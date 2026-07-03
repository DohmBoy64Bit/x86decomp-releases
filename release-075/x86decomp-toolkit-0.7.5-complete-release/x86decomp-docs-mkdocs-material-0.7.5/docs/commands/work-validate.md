---
title: x86decomp work-validate
description: Exact parser-derived reference for x86decomp work-validate in 0.7.5.
---

# `x86decomp work-validate`

## `x86decomp work-validate`

usage: x86decomp work-validate [-h] [--passed]

### Usage

```text
x86decomp work-validate [-h] [--passed]
                               database task_id validator report_path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `task_id` | required. No help text is declared; parser destination is `task_id`. |
| `validator` | required. No help text is declared; parser destination is `validator`. |
| `report_path` | required. No help text is declared; parser destination is `report_path`. |
| `--passed` | default: `False` · nargs: `0`. No help text is declared; parser destination is `passed`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

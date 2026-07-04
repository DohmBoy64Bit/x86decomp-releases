---
title: x86decomp work-claim
description: Exact parser-derived reference for x86decomp work-claim in 0.7.5.
---

# `x86decomp work-claim`

## `x86decomp work-claim`

usage: x86decomp work-claim [-h] database task_id assignee

### Usage

```text
x86decomp work-claim [-h] database task_id assignee
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `task_id` | required. No help text is declared; parser destination is `task_id`. |
| `assignee` | required. No help text is declared; parser destination is `assignee`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

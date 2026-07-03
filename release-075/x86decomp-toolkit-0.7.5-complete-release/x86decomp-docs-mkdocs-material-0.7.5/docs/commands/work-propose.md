---
title: x86decomp work-propose
description: Exact parser-derived reference for x86decomp work-propose in 0.7.5.
---

# `x86decomp work-propose`

## `x86decomp work-propose`

usage: x86decomp work-propose [-h] --evidence EVIDENCE

### Usage

```text
x86decomp work-propose [-h] --evidence EVIDENCE
                              database task_id proposal
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `task_id` | required. No help text is declared; parser destination is `task_id`. |
| `proposal` | required · type: `_path`. No help text is declared; parser destination is `proposal`. |
| `--evidence` | required. No help text is declared; parser destination is `evidence`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

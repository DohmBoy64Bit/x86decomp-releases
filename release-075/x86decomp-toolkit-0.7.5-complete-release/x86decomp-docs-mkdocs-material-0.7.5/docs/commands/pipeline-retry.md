---
title: x86decomp pipeline-retry
description: Exact parser-derived reference for x86decomp pipeline-retry in 0.7.5.
---

# `x86decomp pipeline-retry`

## `x86decomp pipeline-retry`

usage: x86decomp pipeline-retry [-h] [--cascade] project pipeline_id stage_id

### Usage

```text
x86decomp pipeline-retry [-h] [--cascade] project pipeline_id stage_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `pipeline_id` | required. No help text is declared; parser destination is `pipeline_id`. |
| `stage_id` | required. No help text is declared; parser destination is `stage_id`. |
| `--cascade` | default: `False` · nargs: `0`. No help text is declared; parser destination is `cascade`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

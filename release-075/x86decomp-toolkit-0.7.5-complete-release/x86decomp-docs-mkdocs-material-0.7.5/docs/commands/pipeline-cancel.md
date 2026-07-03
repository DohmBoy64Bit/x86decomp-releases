---
title: x86decomp pipeline-cancel
description: Exact parser-derived reference for x86decomp pipeline-cancel in 0.7.5.
---

# `x86decomp pipeline-cancel`

## `x86decomp pipeline-cancel`

usage: x86decomp pipeline-cancel [-h] [--stage-id STAGE_ID]

### Usage

```text
x86decomp pipeline-cancel [-h] [--stage-id STAGE_ID]
                                 project pipeline_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `pipeline_id` | required. No help text is declared; parser destination is `pipeline_id`. |
| `--stage-id` | declared. No help text is declared; parser destination is `stage_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

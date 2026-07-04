---
title: x86decomp pipeline-recover
description: Exact parser-derived reference for x86decomp pipeline-recover in 0.7.5.
---

# `x86decomp pipeline-recover`

## `x86decomp pipeline-recover`

usage: x86decomp pipeline-recover [-h] [--pipeline-id PIPELINE_ID]

### Usage

```text
x86decomp pipeline-recover [-h] [--pipeline-id PIPELINE_ID]
                                  [--stale-seconds STALE_SECONDS]
                                  project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--pipeline-id` | declared. No help text is declared; parser destination is `pipeline_id`. |
| `--stale-seconds` | default: `600` · type: `int`. No help text is declared; parser destination is `stale_seconds`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

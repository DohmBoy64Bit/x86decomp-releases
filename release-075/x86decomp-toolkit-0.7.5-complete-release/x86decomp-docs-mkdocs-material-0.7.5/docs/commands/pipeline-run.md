---
title: x86decomp pipeline-run
description: Exact parser-derived reference for x86decomp pipeline-run in 0.7.5.
---

# `x86decomp pipeline-run`

## `x86decomp pipeline-run`

usage: x86decomp pipeline-run [-h] [--continue-on-failure] project manifest

### Usage

```text
x86decomp pipeline-run [-h] [--continue-on-failure] project manifest
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `manifest` | required · type: `_path`. No help text is declared; parser destination is `manifest`. |
| `--continue-on-failure` | default: `False` · nargs: `0`. No help text is declared; parser destination is `continue_on_failure`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

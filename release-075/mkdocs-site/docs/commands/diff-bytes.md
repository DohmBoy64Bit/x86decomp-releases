---
title: x86decomp diff-bytes
description: Exact parser-derived reference for x86decomp diff-bytes in 0.7.5.
---

# `x86decomp diff-bytes`

## `x86decomp diff-bytes`

usage: x86decomp diff-bytes [-h] [--report REPORT]

### Usage

```text
x86decomp diff-bytes [-h] [--report REPORT]
                            [--max-mismatches MAX_MISMATCHES]
                            target candidate
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target` | required · type: `_path`. No help text is declared; parser destination is `target`. |
| `candidate` | required · type: `_path`. No help text is declared; parser destination is `candidate`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |
| `--max-mismatches` | default: `64` · type: `int`. No help text is declared; parser destination is `max_mismatches`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

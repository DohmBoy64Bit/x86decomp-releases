---
title: x86decomp memory-add
description: Exact parser-derived reference for x86decomp memory-add in 0.7.5.
---

# `x86decomp memory-add`

## `x86decomp memory-add`

usage: x86decomp memory-add [-h] --actor ACTOR --category CATEGORY

### Usage

```text
x86decomp memory-add [-h] --actor ACTOR --category CATEGORY
                            --summary SUMMARY [--details-json DETAILS_JSON]
                            [--evidence EVIDENCE]
                            project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--actor` | required. No help text is declared; parser destination is `actor`. |
| `--category` | required. No help text is declared; parser destination is `category`. |
| `--summary` | required. No help text is declared; parser destination is `summary`. |
| `--details-json` | default: `'{}'`. No help text is declared; parser destination is `details_json`. |
| `--evidence` | default: `[]`. No help text is declared; parser destination is `evidence`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

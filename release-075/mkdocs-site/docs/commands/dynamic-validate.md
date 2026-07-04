---
title: x86decomp dynamic-validate
description: Exact parser-derived reference for x86decomp dynamic-validate in 0.7.5.
---

# `x86decomp dynamic-validate`

## `x86decomp dynamic-validate`

usage: x86decomp dynamic-validate [-h] [--target-base TARGET_BASE]

### Usage

```text
x86decomp dynamic-validate [-h] [--target-base TARGET_BASE]
                                  [--candidate-base CANDIDATE_BASE]
                                  [--report REPORT]
                                  target candidate harness
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target` | required · type: `_path`. No help text is declared; parser destination is `target`. |
| `candidate` | required · type: `_path`. No help text is declared; parser destination is `candidate`. |
| `harness` | required · type: `_path`. No help text is declared; parser destination is `harness`. |
| `--target-base` | type: `_int`. No help text is declared; parser destination is `target_base`. |
| `--candidate-base` | type: `_int`. No help text is declared; parser destination is `candidate_base`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

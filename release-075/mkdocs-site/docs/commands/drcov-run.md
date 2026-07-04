---
title: x86decomp drcov-run
description: Exact parser-derived reference for x86decomp drcov-run in 0.7.5.
---

# `x86decomp drcov-run`

## `x86decomp drcov-run`

usage: x86decomp drcov-run [-h] [--drrun DRRUN] [--program-arg PROGRAM_ARG]

### Usage

```text
x86decomp drcov-run [-h] [--drrun DRRUN] [--program-arg PROGRAM_ARG]
                           [--timeout TIMEOUT] [--report REPORT]
                           executable output_directory
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `executable` | required · type: `_path`. No help text is declared; parser destination is `executable`. |
| `output_directory` | required · type: `_path`. No help text is declared; parser destination is `output_directory`. |
| `--drrun` | type: `_path`. No help text is declared; parser destination is `drrun`. |
| `--program-arg` | default: `[]`. No help text is declared; parser destination is `program_arg`. |
| `--timeout` | default: `300` · type: `int`. No help text is declared; parser destination is `timeout`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

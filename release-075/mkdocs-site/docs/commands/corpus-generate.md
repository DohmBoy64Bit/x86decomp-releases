---
title: x86decomp corpus-generate
description: Exact parser-derived reference for x86decomp corpus-generate in 0.7.5.
---

# `x86decomp corpus-generate`

## `x86decomp corpus-generate`

usage: x86decomp corpus-generate [-h] [--cases-per-family CASES_PER_FAMILY]

### Usage

```text
x86decomp corpus-generate [-h] [--cases-per-family CASES_PER_FAMILY]
                                 [--seed SEED] [--c-only] [--cpp-only]
                                 [--report REPORT]
                                 output_directory
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output_directory` | required · type: `_path`. No help text is declared; parser destination is `output_directory`. |
| `--cases-per-family` | default: `8` · type: `int`. No help text is declared; parser destination is `cases_per_family`. |
| `--seed` | default: `2262745310` · type: `_int`. No help text is declared; parser destination is `seed`. |
| `--c-only` | default: `False` · nargs: `0`. No help text is declared; parser destination is `c_only`. |
| `--cpp-only` | default: `False` · nargs: `0`. No help text is declared; parser destination is `cpp_only`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

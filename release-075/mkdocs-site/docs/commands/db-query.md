---
title: x86decomp db-query
description: Exact parser-derived reference for x86decomp db-query in 0.7.5.
---

# `x86decomp db-query`

## `x86decomp db-query`

usage: x86decomp db-query [-h] [--parameters-json PARAMETERS_JSON]

### Usage

```text
x86decomp db-query [-h] [--parameters-json PARAMETERS_JSON]
                          database sql
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `sql` | required. No help text is declared; parser destination is `sql`. |
| `--parameters-json` | default: `'[]'`. No help text is declared; parser destination is `parameters_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

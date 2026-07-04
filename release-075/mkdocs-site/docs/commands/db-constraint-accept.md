---
title: x86decomp db-constraint-accept
description: Exact parser-derived reference for x86decomp db-constraint-accept in
  0.7.5.
---

# `x86decomp db-constraint-accept`

## `x86decomp db-constraint-accept`

usage: x86decomp db-constraint-accept [-h] database constraint_id

### Usage

```text
x86decomp db-constraint-accept [-h] database constraint_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `constraint_id` | required · type: `int`. No help text is declared; parser destination is `constraint_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

---
title: x86decomp claim-create
description: Exact parser-derived reference for x86decomp claim-create in 0.7.5.
---

# `x86decomp claim-create`

## `x86decomp claim-create`

usage: x86decomp claim-create [-h] --subject SUBJECT --predicate PREDICATE

### Usage

```text
x86decomp claim-create [-h] --subject SUBJECT --predicate PREDICATE
                              --object OBJECT_VALUE [--evidence EVIDENCE]
                              [--id ID]
                              project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--subject` | required. No help text is declared; parser destination is `subject`. |
| `--predicate` | required. No help text is declared; parser destination is `predicate`. |
| `--object` | required. No help text is declared; parser destination is `object_value`. |
| `--evidence` | default: `[]`. No help text is declared; parser destination is `evidence`. |
| `--id` | declared. No help text is declared; parser destination is `id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

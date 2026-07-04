---
title: x86decomp work-validate
description: Exact v0.7.8 parser-derived reference for `x86decomp work-validate`.
---


# `x86decomp work-validate`

## Usage

```text
usage: x86decomp work-validate [-h] [--passed]
                               database task_id validator report_path
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path` · parser destination: `database`. No help text declared. |
| `task_id` | required · parser destination: `task_id`. No help text declared. |
| `validator` | required · parser destination: `validator`. No help text declared. |
| `report_path` | required · parser destination: `report_path`. No help text declared. |
| `--passed` | nargs: `0` · default: `False` · parser destination: `passed`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

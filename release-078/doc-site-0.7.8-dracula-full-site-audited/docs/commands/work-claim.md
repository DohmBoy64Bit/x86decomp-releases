---
title: x86decomp work-claim
description: Exact v0.7.8 parser-derived reference for `x86decomp work-claim`.
---


# `x86decomp work-claim`

## Usage

```text
usage: x86decomp work-claim [-h] database task_id assignee
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path` · parser destination: `database`. No help text declared. |
| `task_id` | required · parser destination: `task_id`. No help text declared. |
| `assignee` | required · parser destination: `assignee`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

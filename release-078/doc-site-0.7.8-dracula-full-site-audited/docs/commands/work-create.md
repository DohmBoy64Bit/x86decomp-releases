---
title: x86decomp work-create
description: Exact v0.7.8 parser-derived reference for `x86decomp work-create`.
---


# `x86decomp work-create`

## Usage

```text
usage: x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY]
                             database function_id {matching,functional} kind
                             instructions
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path` · parser destination: `database`. No help text declared. |
| `function_id` | required · parser destination: `function_id`. No help text declared. |
| `mode` | required · choices: `matching`, `functional` · parser destination: `mode`. No help text declared. |
| `kind` | required · parser destination: `kind`. No help text declared. |
| `instructions` | required · parser destination: `instructions`. No help text declared. |
| `--validator` | required · parser destination: `validator`. No help text declared. |
| `--priority` | type: `int` · default: `0` · parser destination: `priority`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

---
title: x86decomp db-query
description: Exact v0.7.8 parser-derived reference for `x86decomp db-query`.
---


# `x86decomp db-query`

## Usage

```text
usage: x86decomp db-query [-h] [--parameters-json PARAMETERS_JSON]
                          database sql
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path` · parser destination: `database`. No help text declared. |
| `sql` | required · parser destination: `sql`. No help text declared. |
| `--parameters-json` | default: `'[]'` · parser destination: `parameters_json`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

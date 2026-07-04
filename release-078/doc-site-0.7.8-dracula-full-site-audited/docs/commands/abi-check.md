---
title: x86decomp abi-check
description: Exact v0.7.8 parser-derived reference for `x86decomp abi-check`.
---


# `x86decomp abi-check`

## Usage

```text
usage: x86decomp abi-check [-h] [--base BASE] [--report REPORT] code contract
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `code` | required · type: `_path` · parser destination: `code`. No help text declared. |
| `contract` | required · type: `_path` · parser destination: `contract`. No help text declared. |
| `--base` | type: `_int` · default: `0` · parser destination: `base`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

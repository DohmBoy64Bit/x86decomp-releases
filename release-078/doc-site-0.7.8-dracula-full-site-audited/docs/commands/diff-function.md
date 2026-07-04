---
title: x86decomp diff-function
description: Exact v0.7.8 parser-derived reference for `x86decomp diff-function`.
---


# `x86decomp diff-function`

## Usage

```text
usage: x86decomp diff-function [-h] [--report REPORT] pe rva size coff symbol
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path` · parser destination: `pe`. No help text declared. |
| `rva` | required · type: `_int` · parser destination: `rva`. No help text declared. |
| `size` | required · type: `_int` · parser destination: `size`. No help text declared. |
| `coff` | required · type: `_path` · parser destination: `coff`. No help text declared. |
| `symbol` | required · parser destination: `symbol`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

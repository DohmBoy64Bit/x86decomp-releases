---
title: x86decomp image-match
description: Exact v0.7.8 parser-derived reference for `x86decomp image-match`.
---


# `x86decomp image-match`

## Usage

```text
usage: x86decomp image-match [-h] [--profile PROFILE] [--report REPORT]
                             reference candidate
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `reference` | required · type: `_path` · parser destination: `reference`. No help text declared. |
| `candidate` | required · type: `_path` · parser destination: `candidate`. No help text declared. |
| `--profile` | type: `_path` · parser destination: `profile`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

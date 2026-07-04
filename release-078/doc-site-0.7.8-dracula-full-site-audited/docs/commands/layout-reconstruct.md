---
title: x86decomp layout-reconstruct
description: Exact v0.7.8 parser-derived reference for `x86decomp layout-reconstruct`.
---


# `x86decomp layout-reconstruct`

## Usage

```text
usage: x86decomp layout-reconstruct [-h] [--report REPORT]
                                    pe map [objects ...]
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path` · parser destination: `pe`. No help text declared. |
| `map` | required · type: `_path` · parser destination: `map`. No help text declared. |
| `objects` | nargs: `*` · type: `_path` · parser destination: `objects`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

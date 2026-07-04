---
title: x86decomp compile
description: Exact v0.7.8 parser-derived reference for `x86decomp compile`.
---


# `x86decomp compile`

## Usage

```text
usage: x86decomp compile [-h] [--report REPORT] [--extra-arg EXTRA_ARG]
                         [--cache CACHE]
                         profile source output
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · type: `_path` · parser destination: `profile`. No help text declared. |
| `source` | required · type: `_path` · parser destination: `source`. No help text declared. |
| `output` | required · type: `_path` · parser destination: `output`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |
| `--extra-arg` | default: `[]` · parser destination: `extra_arg`. No help text declared. |
| `--cache` | type: `_path` · parser destination: `cache`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

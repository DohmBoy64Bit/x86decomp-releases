---
title: x86decomp cpp-recover
description: Exact v0.7.8 parser-derived reference for `x86decomp cpp-recover`.
---


# `x86decomp cpp-recover`

## Usage

```text
usage: x86decomp cpp-recover [-h] [--metadata-report METADATA_REPORT]
                             [--object OBJECT] [--map MAP] [--report REPORT]
                             pe
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path` · parser destination: `pe`. No help text declared. |
| `--metadata-report` | type: `_path` · parser destination: `metadata_report`. No help text declared. |
| `--object` | type: `_path` · default: `[]` · parser destination: `object`. No help text declared. |
| `--map` | type: `_path` · parser destination: `map`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

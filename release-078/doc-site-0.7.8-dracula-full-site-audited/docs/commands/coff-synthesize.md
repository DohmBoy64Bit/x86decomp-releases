---
title: x86decomp coff-synthesize
description: Exact v0.7.8 parser-derived reference for `x86decomp coff-synthesize`.
---


# `x86decomp coff-synthesize`

## Usage

```text
usage: x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}]
                                 [--relocations RELOCATIONS]
                                 code symbol output
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `code` | required · type: `_path` · parser destination: `code`. No help text declared. |
| `symbol` | required · parser destination: `symbol`. No help text declared. |
| `output` | required · type: `_path` · parser destination: `output`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--relocations` | type: `_path` · parser destination: `relocations`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

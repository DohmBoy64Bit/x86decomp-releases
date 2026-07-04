---
title: x86decomp toolchain-register
description: Exact v0.7.8 parser-derived reference for `x86decomp toolchain-register`.
---


# `x86decomp toolchain-register`

## Usage

```text
usage: x86decomp toolchain-register [-h] --executable EXECUTABLE
                                    registry toolchain_id family version
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `registry` | required · type: `_path` · parser destination: `registry`. No help text declared. |
| `toolchain_id` | required · parser destination: `toolchain_id`. No help text declared. |
| `family` | required · parser destination: `family`. No help text declared. |
| `version` | required · parser destination: `version`. No help text declared. |
| `--executable` | required · parser destination: `executable`. role=path |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

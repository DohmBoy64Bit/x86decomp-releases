---
title: x86decomp project-from-target
description: Exact v0.7.8 parser-derived reference for `x86decomp project-from-target`.
---


# `x86decomp project-from-target`

## Usage

```text
usage: x86decomp project-from-target [-h] [--reference-binary]
                                     target_pack project
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target_pack` | required · type: `_path` · parser destination: `target_pack`. No help text declared. |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `--reference-binary` | nargs: `0` · default: `False` · parser destination: `reference_binary`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

---
title: x86decomp corpus-generate
description: Exact v0.7.8 parser-derived reference for `x86decomp corpus-generate`.
---


# `x86decomp corpus-generate`

## Usage

```text
usage: x86decomp corpus-generate [-h] [--cases-per-family CASES_PER_FAMILY]
                                 [--seed SEED] [--c-only] [--cpp-only]
                                 [--report REPORT]
                                 output_directory
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output_directory` | required · type: `_path` · parser destination: `output_directory`. No help text declared. |
| `--cases-per-family` | type: `int` · default: `8` · parser destination: `cases_per_family`. No help text declared. |
| `--seed` | type: `_int` · default: `2262745310` · parser destination: `seed`. No help text declared. |
| `--c-only` | nargs: `0` · default: `False` · parser destination: `c_only`. No help text declared. |
| `--cpp-only` | nargs: `0` · default: `False` · parser destination: `cpp_only`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

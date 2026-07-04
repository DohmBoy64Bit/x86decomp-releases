---
title: x86decomp dependency-audit
description: Exact v0.7.8 parser-derived reference for `x86decomp dependency-audit`.
---


# `x86decomp dependency-audit`

## Usage

```text
usage: x86decomp dependency-audit [-h] [--executable EXECUTABLE]
                                  [--timeout TIMEOUT] [--report REPORT]
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--executable` | default: `'pip-audit'` · parser destination: `executable`. No help text declared. |
| `--timeout` | type: `int` · default: `300` · parser destination: `timeout`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

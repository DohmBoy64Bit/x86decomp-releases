---
title: x86decomp diff-bytes
description: Exact v0.7.8 parser-derived reference for `x86decomp diff-bytes`.
---


# `x86decomp diff-bytes`

## Usage

```text
usage: x86decomp diff-bytes [-h] [--report REPORT]
                            [--max-mismatches MAX_MISMATCHES]
                            target candidate
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target` | required · type: `_path` · parser destination: `target`. No help text declared. |
| `candidate` | required · type: `_path` · parser destination: `candidate`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |
| `--max-mismatches` | type: `int` · default: `64` · parser destination: `max_mismatches`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

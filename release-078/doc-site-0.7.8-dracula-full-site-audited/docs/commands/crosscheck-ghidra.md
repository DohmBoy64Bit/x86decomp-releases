---
title: x86decomp crosscheck-ghidra
description: Exact v0.7.8 parser-derived reference for `x86decomp crosscheck-ghidra`.
---


# `x86decomp crosscheck-ghidra`

## Usage

```text
usage: x86decomp crosscheck-ghidra [-h] --base BASE
                                   [--architecture {x86,x86_64}]
                                   [--report REPORT]
                                   instructions_jsonl code
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `instructions_jsonl` | required · type: `_path` · parser destination: `instructions_jsonl`. No help text declared. |
| `code` | required · type: `_path` · parser destination: `code`. No help text declared. |
| `--base` | required · type: `_int` · parser destination: `base`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

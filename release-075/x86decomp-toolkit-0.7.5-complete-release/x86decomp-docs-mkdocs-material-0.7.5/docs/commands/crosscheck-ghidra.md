---
title: x86decomp crosscheck-ghidra
description: Exact parser-derived reference for x86decomp crosscheck-ghidra in 0.7.5.
---

# `x86decomp crosscheck-ghidra`

## `x86decomp crosscheck-ghidra`

usage: x86decomp crosscheck-ghidra [-h] --base BASE

### Usage

```text
x86decomp crosscheck-ghidra [-h] --base BASE
                                   [--architecture {x86,x86_64}]
                                   [--report REPORT]
                                   instructions_jsonl code
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `instructions_jsonl` | required · type: `_path`. No help text is declared; parser destination is `instructions_jsonl`. |
| `code` | required · type: `_path`. No help text is declared; parser destination is `code`. |
| `--base` | required · type: `_int`. No help text is declared; parser destination is `base`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

---
title: x86decomp coff-synthesize
description: Exact parser-derived reference for x86decomp coff-synthesize in 0.7.5.
---

# `x86decomp coff-synthesize`

## `x86decomp coff-synthesize`

usage: x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}]

### Usage

```text
x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}]
                                 [--relocations RELOCATIONS]
                                 code symbol output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `code` | required · type: `_path`. No help text is declared; parser destination is `code`. |
| `symbol` | required. No help text is declared; parser destination is `symbol`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |
| `--relocations` | type: `_path`. No help text is declared; parser destination is `relocations`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

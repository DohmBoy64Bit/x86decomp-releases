---
title: x86decomp toolchain-register
description: Exact parser-derived reference for x86decomp toolchain-register in 0.7.5.
---

# `x86decomp toolchain-register`

## `x86decomp toolchain-register`

usage: x86decomp toolchain-register [-h] --executable EXECUTABLE

### Usage

```text
x86decomp toolchain-register [-h] --executable EXECUTABLE
                                    registry toolchain_id family version
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `registry` | required · type: `_path`. No help text is declared; parser destination is `registry`. |
| `toolchain_id` | required. No help text is declared; parser destination is `toolchain_id`. |
| `family` | required. No help text is declared; parser destination is `family`. |
| `version` | required. No help text is declared; parser destination is `version`. |
| `--executable` | required. role=path |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

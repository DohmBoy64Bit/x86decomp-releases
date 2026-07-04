---
title: x86decomp project-from-target
description: Exact parser-derived reference for x86decomp project-from-target in 0.7.5.
---

# `x86decomp project-from-target`

## `x86decomp project-from-target`

usage: x86decomp project-from-target [-h] [--reference-binary]

### Usage

```text
x86decomp project-from-target [-h] [--reference-binary]
                                     target_pack project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target_pack` | required · type: `_path`. No help text is declared; parser destination is `target_pack`. |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--reference-binary` | default: `False` · nargs: `0`. No help text is declared; parser destination is `reference_binary`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

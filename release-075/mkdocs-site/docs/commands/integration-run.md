---
title: x86decomp integration-run
description: Exact parser-derived reference for x86decomp integration-run in 0.7.5.
---

# `x86decomp integration-run`

## `x86decomp integration-run`

usage: x86decomp integration-run [-h] [--allow-host-execution]

### Usage

```text
x86decomp integration-run [-h] [--allow-host-execution]
                                 [--report REPORT]
                                 manifest
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required · type: `_path`. No help text is declared; parser destination is `manifest`. |
| `--allow-host-execution` | default: `False` · nargs: `0`. No help text is declared; parser destination is `allow_host_execution`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

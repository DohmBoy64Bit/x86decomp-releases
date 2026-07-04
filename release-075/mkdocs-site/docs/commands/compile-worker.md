---
title: x86decomp compile-worker
description: Exact parser-derived reference for x86decomp compile-worker in 0.7.5.
---

# `x86decomp compile-worker`

## `x86decomp compile-worker`

usage: x86decomp compile-worker [-h] [--isolation {local_bounded,container}]

### Usage

```text
x86decomp compile-worker [-h] [--isolation {local_bounded,container}]
                                [--container-image CONTAINER_IMAGE]
                                [--cache CACHE] [--report REPORT]
                                profile source output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · type: `_path`. No help text is declared; parser destination is `profile`. |
| `source` | required · type: `_path`. No help text is declared; parser destination is `source`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--isolation` | default: `'local_bounded'` · choices: `local_bounded`, `container`. No help text is declared; parser destination is `isolation`. |
| `--container-image` | declared. No help text is declared; parser destination is `container_image`. |
| `--cache` | type: `_path`. No help text is declared; parser destination is `cache`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

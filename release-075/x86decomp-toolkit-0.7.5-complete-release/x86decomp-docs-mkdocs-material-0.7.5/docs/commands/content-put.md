---
title: x86decomp content-put
description: Exact parser-derived reference for x86decomp content-put in 0.7.5.
---

# `x86decomp content-put`

## `x86decomp content-put`

usage: x86decomp content-put [-h] [--media-type MEDIA_TYPE]

### Usage

```text
x86decomp content-put [-h] [--media-type MEDIA_TYPE]
                             [--reference REFERENCE] [--kind KIND]
                             [--owner OWNER]
                             store file
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `store` | required · type: `_path`. No help text is declared; parser destination is `store`. |
| `file` | required · type: `_path`. No help text is declared; parser destination is `file`. |
| `--media-type` | default: `'application/octet-stream'`. No help text is declared; parser destination is `media_type`. |
| `--reference` | declared. No help text is declared; parser destination is `reference`. |
| `--kind` | default: `'artifact'`. No help text is declared; parser destination is `kind`. |
| `--owner` | default: `'user'`. No help text is declared; parser destination is `owner`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

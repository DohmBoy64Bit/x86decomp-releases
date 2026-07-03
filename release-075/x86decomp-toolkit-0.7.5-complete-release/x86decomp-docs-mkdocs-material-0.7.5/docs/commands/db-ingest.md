---
title: x86decomp db-ingest
description: Exact parser-derived reference for x86decomp db-ingest in 0.7.5.
---

# `x86decomp db-ingest`

## `x86decomp db-ingest`

usage: x86decomp db-ingest [-h] [--image-base IMAGE_BASE] database artifact

### Usage

```text
x86decomp db-ingest [-h] [--image-base IMAGE_BASE] database artifact
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `artifact` | required · type: `_path`. No help text is declared; parser destination is `artifact`. |
| `--image-base` | default: `0` · type: `_int`. No help text is declared; parser destination is `image_base`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

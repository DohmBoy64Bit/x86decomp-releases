---
title: x86decomp db-ingest
description: Exact v0.7.8 parser-derived reference for `x86decomp db-ingest`.
---


# `x86decomp db-ingest`

## Usage

```text
usage: x86decomp db-ingest [-h] [--image-base IMAGE_BASE] database artifact
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path` · parser destination: `database`. No help text declared. |
| `artifact` | required · type: `_path` · parser destination: `artifact`. No help text declared. |
| `--image-base` | type: `_int` · default: `0` · parser destination: `image_base`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

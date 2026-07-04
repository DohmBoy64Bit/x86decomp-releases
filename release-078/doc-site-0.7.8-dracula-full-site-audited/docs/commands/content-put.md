---
title: x86decomp content-put
description: Exact v0.7.8 parser-derived reference for `x86decomp content-put`.
---


# `x86decomp content-put`

## Usage

```text
usage: x86decomp content-put [-h] [--media-type MEDIA_TYPE]
                             [--reference REFERENCE] [--kind KIND]
                             [--owner OWNER]
                             store file
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `store` | required · type: `_path` · parser destination: `store`. No help text declared. |
| `file` | required · type: `_path` · parser destination: `file`. No help text declared. |
| `--media-type` | default: `'application/octet-stream'` · parser destination: `media_type`. No help text declared. |
| `--reference` | parser destination: `reference`. No help text declared. |
| `--kind` | default: `'artifact'` · parser destination: `kind`. No help text declared. |
| `--owner` | default: `'user'` · parser destination: `owner`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

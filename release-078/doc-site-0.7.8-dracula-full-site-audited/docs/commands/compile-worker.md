---
title: x86decomp compile-worker
description: Exact v0.7.8 parser-derived reference for `x86decomp compile-worker`.
---


# `x86decomp compile-worker`

## Usage

```text
usage: x86decomp compile-worker [-h] [--isolation {local_bounded,container}]
                                [--container-image CONTAINER_IMAGE]
                                [--cache CACHE] [--report REPORT]
                                profile source output
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · type: `_path` · parser destination: `profile`. No help text declared. |
| `source` | required · type: `_path` · parser destination: `source`. No help text declared. |
| `output` | required · type: `_path` · parser destination: `output`. No help text declared. |
| `--isolation` | choices: `local_bounded`, `container` · default: `'local_bounded'` · parser destination: `isolation`. No help text declared. |
| `--container-image` | parser destination: `container_image`. No help text declared. |
| `--cache` | type: `_path` · parser destination: `cache`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

---
title: x86decomp integration-run
description: Exact v0.7.8 parser-derived reference for `x86decomp integration-run`.
---


# `x86decomp integration-run`

## Usage

```text
usage: x86decomp integration-run [-h] [--allow-host-execution]
                                 [--report REPORT]
                                 manifest
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required · type: `_path` · parser destination: `manifest`. No help text declared. |
| `--allow-host-execution` | nargs: `0` · default: `False` · parser destination: `allow_host_execution`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

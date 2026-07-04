---
title: x86decomp pipeline-run
description: Exact v0.7.8 parser-derived reference for `x86decomp pipeline-run`.
---


# `x86decomp pipeline-run`

## Usage

```text
usage: x86decomp pipeline-run [-h] [--continue-on-failure] project manifest
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `manifest` | required · type: `_path` · parser destination: `manifest`. No help text declared. |
| `--continue-on-failure` | nargs: `0` · default: `False` · parser destination: `continue_on_failure`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

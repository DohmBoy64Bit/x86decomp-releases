---
title: x86decomp project-migrate
description: Exact v0.7.8 parser-derived reference for `x86decomp project-migrate`.
---


# `x86decomp project-migrate`

## Usage

```text
usage: x86decomp project-migrate [-h] [--dry-run] [--backup BACKUP] project
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `--dry-run` | nargs: `0` · default: `False` · parser destination: `dry_run`. No help text declared. |
| `--backup` | type: `_path` · parser destination: `backup`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

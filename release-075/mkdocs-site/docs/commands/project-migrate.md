---
title: x86decomp project-migrate
description: Exact parser-derived reference for x86decomp project-migrate in 0.7.5.
---

# `x86decomp project-migrate`

## `x86decomp project-migrate`

usage: x86decomp project-migrate [-h] [--dry-run] [--backup BACKUP] project

### Usage

```text
x86decomp project-migrate [-h] [--dry-run] [--backup BACKUP] project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--dry-run` | default: `False` · nargs: `0`. No help text is declared; parser destination is `dry_run`. |
| `--backup` | type: `_path`. No help text is declared; parser destination is `backup`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

---
title: x86decomp project-migrate
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/project-migrate.html
---

<a id="command-project-migrate"></a>

Section: Command reference

# `x86decomp project-migrate`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp project-migrate --help
```

Metadata: current · core

## `x86decomp project-migrate`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp project-migrate [-h] [--dry-run] [--backup BACKUP] project
```

### Syntax example

```
x86decomp project-migrate ./work
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--dry-run` nargs: 0 · default: False | No argument help text is declared; parser destination is `dry_run`. |
| `--backup` type: _path | No argument help text is declared; parser destination is `backup`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

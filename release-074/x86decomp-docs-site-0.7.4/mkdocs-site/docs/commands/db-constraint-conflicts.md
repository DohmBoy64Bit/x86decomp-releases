---
title: x86decomp db-constraint-conflicts
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/db-constraint-conflicts.html
---

<a id="command-db-constraint-conflicts"></a>

Section: Command reference

# `x86decomp db-constraint-conflicts`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp db-constraint-conflicts --help
```

Metadata: current · core

## `x86decomp db-constraint-conflicts`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp db-constraint-conflicts [-h] database subject relation
```

### Syntax example

```
x86decomp db-constraint-conflicts ./analysis.db example example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `subject` required | No argument help text is declared; parser destination is `subject`. |
| `relation` required | No argument help text is declared; parser destination is `relation`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

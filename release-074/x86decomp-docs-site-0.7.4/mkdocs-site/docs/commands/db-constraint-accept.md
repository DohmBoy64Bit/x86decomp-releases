---
title: x86decomp db-constraint-accept
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/db-constraint-accept.html
---

<a id="command-db-constraint-accept"></a>

Section: Command reference

# `x86decomp db-constraint-accept`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp db-constraint-accept --help
```

Metadata: current · core

## `x86decomp db-constraint-accept`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp db-constraint-accept [-h] database constraint_id
```

### Syntax example

```
x86decomp db-constraint-accept ./analysis.db 1
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `constraint_id` required · type: int | No argument help text is declared; parser destination is `constraint_id`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

---
title: x86decomp db-query
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/db-query.html
---

<a id="command-db-query"></a>

Section: Command reference

# `x86decomp db-query`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp db-query --help
```

Metadata: current · core

## `x86decomp db-query`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp db-query [-h] [--parameters-json PARAMETERS_JSON]
                          database sql
```

### Syntax example

```
x86decomp db-query ./analysis.db example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `sql` required | No argument help text is declared; parser destination is `sql`. |
| `--parameters-json` default: '[]' | No argument help text is declared; parser destination is `parameters_json`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

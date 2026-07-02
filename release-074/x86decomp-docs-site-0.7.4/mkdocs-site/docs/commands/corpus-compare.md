---
title: x86decomp corpus-compare
description: compare compiler/version ground-truth corpus reports
original_path: commands/corpus-compare.html
---

<a id="command-corpus-compare"></a>

Section: Command reference

# `x86decomp corpus-compare`

compare compiler/version ground-truth corpus reports

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp corpus-compare --help
```

Metadata: current · core

## `x86decomp corpus-compare`

compare compiler/version ground-truth corpus reports

### Usage

```
x86decomp corpus-compare [-h] [--report REPORT] reports [reports ...]
```

### Syntax example

```
x86decomp corpus-compare ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `reports` required · nargs: + · type: _path | No argument help text is declared; parser destination is `reports`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

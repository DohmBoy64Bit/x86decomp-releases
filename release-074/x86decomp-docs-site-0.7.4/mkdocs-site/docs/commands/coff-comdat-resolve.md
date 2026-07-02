---
title: x86decomp coff-comdat-resolve
description: resolve COMDAT groups across COFF objects
original_path: commands/coff-comdat-resolve.html
---

<a id="command-coff-comdat-resolve"></a>

Section: Command reference

# `x86decomp coff-comdat-resolve`

resolve COMDAT groups across COFF objects

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp coff-comdat-resolve --help
```

Metadata: current · core

## `x86decomp coff-comdat-resolve`

resolve COMDAT groups across COFF objects

### Usage

```
x86decomp coff-comdat-resolve [-h] [--report REPORT]
                                     objects [objects ...]
```

### Syntax example

```
x86decomp coff-comdat-resolve ./candidate.obj
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `objects` required · nargs: + · type: _path | No argument help text is declared; parser destination is `objects`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

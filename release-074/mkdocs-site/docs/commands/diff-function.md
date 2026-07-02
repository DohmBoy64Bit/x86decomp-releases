---
title: x86decomp diff-function
description: compare a linked PE function to a COFF symbol
original_path: commands/diff-function.html
---

<a id="command-diff-function"></a>

Section: Command reference

# `x86decomp diff-function`

compare a linked PE function to a COFF symbol

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp diff-function --help
```

Metadata: current · core

## `x86decomp diff-function`

compare a linked PE function to a COFF symbol

### Usage

```
x86decomp diff-function [-h] [--report REPORT] pe rva size coff symbol
```

### Syntax example

```
x86decomp diff-function ./target.exe 0x1000 1 ./candidate.obj example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `pe` required · type: _path | No argument help text is declared; parser destination is `pe`. |
| `rva` required · type: _int | No argument help text is declared; parser destination is `rva`. |
| `size` required · type: _int | No argument help text is declared; parser destination is `size`. |
| `coff` required · type: _path | No argument help text is declared; parser destination is `coff`. |
| `symbol` required | No argument help text is declared; parser destination is `symbol`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

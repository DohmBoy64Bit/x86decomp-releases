---
title: x86decomp corpus-build
description: build a reproducible compiler/version ground-truth corpus
original_path: commands/corpus-build.html
---

<a id="command-corpus-build"></a>

Section: Command reference

# `x86decomp corpus-build`

build a reproducible compiler/version ground-truth corpus

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp corpus-build --help
```

Metadata: current · core

## `x86decomp corpus-build`

build a reproducible compiler/version ground-truth corpus

### Usage

```
x86decomp corpus-build [-h] [--report REPORT] manifest output_directory
```

### Syntax example

```
x86decomp corpus-build ./output.json ./output
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `manifest` required · type: _path | No argument help text is declared; parser destination is `manifest`. |
| `output_directory` required · type: _path | No argument help text is declared; parser destination is `output_directory`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

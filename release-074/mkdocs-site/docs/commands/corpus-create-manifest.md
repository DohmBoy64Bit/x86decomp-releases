---
title: x86decomp corpus-create-manifest
description: create the bundled compiler ground-truth manifest
original_path: commands/corpus-create-manifest.html
---

<a id="command-corpus-create-manifest"></a>

Section: Command reference

# `x86decomp corpus-create-manifest`

create the bundled compiler ground-truth manifest

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp corpus-create-manifest --help
```

Metadata: current · core

## `x86decomp corpus-create-manifest`

create the bundled compiler ground-truth manifest

### Usage

```
x86decomp corpus-create-manifest [-h] repository output
```

### Syntax example

```
x86decomp corpus-create-manifest example ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `repository` required · type: _path | No argument help text is declared; parser destination is `repository`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

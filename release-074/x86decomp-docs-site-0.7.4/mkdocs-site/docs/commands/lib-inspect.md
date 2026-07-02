---
title: x86decomp lib-inspect
description: inspect a COFF archive/static or import library
original_path: commands/lib-inspect.html
---

<a id="command-lib-inspect"></a>

Section: Command reference

# `x86decomp lib-inspect`

inspect a COFF archive/static or import library

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp lib-inspect --help
```

Metadata: current · core

## `x86decomp lib-inspect`

inspect a COFF archive/static or import library

### Usage

```
x86decomp lib-inspect [-h] library
```

### Syntax example

```
x86decomp lib-inspect ./library.lib
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `library` required · type: _path | No argument help text is declared; parser destination is `library`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

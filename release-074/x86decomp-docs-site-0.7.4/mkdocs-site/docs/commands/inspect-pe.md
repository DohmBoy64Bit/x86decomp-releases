---
title: x86decomp inspect-pe
description: parse PE32 or PE32+ metadata
original_path: commands/inspect-pe.html
---

<a id="command-inspect-pe"></a>

Section: Command reference

# `x86decomp inspect-pe`

parse PE32 or PE32+ metadata

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp inspect-pe --help
```

Metadata: current · core

## `x86decomp inspect-pe`

parse PE32 or PE32+ metadata

### Usage

```
x86decomp inspect-pe [-h] binary
```

### Syntax example

```
x86decomp inspect-pe ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `binary` required · type: _path | No argument help text is declared; parser destination is `binary`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

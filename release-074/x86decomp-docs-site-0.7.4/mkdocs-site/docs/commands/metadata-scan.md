---
title: x86decomp metadata-scan
description: recover bounded MSVC RTTI, vtables, unwind, TLS, and initializer metadata
original_path: commands/metadata-scan.html
---

<a id="command-metadata-scan"></a>

Section: Command reference

# `x86decomp metadata-scan`

recover bounded MSVC RTTI, vtables, unwind, TLS, and initializer metadata

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp metadata-scan --help
```

Metadata: current · core

## `x86decomp metadata-scan`

recover bounded MSVC RTTI, vtables, unwind, TLS, and initializer metadata

### Usage

```
x86decomp metadata-scan [-h] [--object OBJECT] [--map MAP]
                               [--report REPORT]
                               pe
```

### Syntax example

```
x86decomp metadata-scan ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `pe` required · type: _path | No argument help text is declared; parser destination is `pe`. |
| `--object` default: [] · type: _path | No argument help text is declared; parser destination is `object`. |
| `--map` type: _path | No argument help text is declared; parser destination is `map`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

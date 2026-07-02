---
title: x86decomp layout-reconstruct
description: correlate PE sections, linker map contributions, and COFF objects
original_path: commands/layout-reconstruct.html
---

<a id="command-layout-reconstruct"></a>

Section: Command reference

# `x86decomp layout-reconstruct`

correlate PE sections, linker map contributions, and COFF objects

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp layout-reconstruct --help
```

Metadata: current · core

## `x86decomp layout-reconstruct`

correlate PE sections, linker map contributions, and COFF objects

### Usage

```
x86decomp layout-reconstruct [-h] [--report REPORT]
                                    pe map [objects ...]
```

### Syntax example

```
x86decomp layout-reconstruct ./target.exe ./target.map
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `pe` required · type: _path | No argument help text is declared; parser destination is `pe`. |
| `map` required · type: _path | No argument help text is declared; parser destination is `map`. |
| `objects` nargs: \* · type: _path | No argument help text is declared; parser destination is `objects`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

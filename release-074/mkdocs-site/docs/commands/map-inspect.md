---
title: x86decomp map-inspect
description: parse an MSVC-compatible linker map
original_path: commands/map-inspect.html
---

<a id="command-map-inspect"></a>

Section: Command reference

# `x86decomp map-inspect`

parse an MSVC-compatible linker map

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp map-inspect --help
```

Metadata: current · core

## `x86decomp map-inspect`

parse an MSVC-compatible linker map

### Usage

```
x86decomp map-inspect [-h] map
```

### Syntax example

```
x86decomp map-inspect ./target.map
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `map` required · type: _path | No argument help text is declared; parser destination is `map`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

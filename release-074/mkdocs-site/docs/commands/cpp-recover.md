---
title: x86decomp cpp-recover
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/cpp-recover.html
---

<a id="command-cpp-recover"></a>

Section: Command reference

# `x86decomp cpp-recover`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp cpp-recover --help
```

Metadata: current · core

## `x86decomp cpp-recover`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp cpp-recover [-h] [--metadata-report METADATA_REPORT]
                             [--object OBJECT] [--map MAP] [--report REPORT]
                             pe
```

### Syntax example

```
x86decomp cpp-recover ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `pe` required · type: _path | No argument help text is declared; parser destination is `pe`. |
| `--metadata-report` type: _path | No argument help text is declared; parser destination is `metadata_report`. |
| `--object` default: [] · type: _path | No argument help text is declared; parser destination is `object`. |
| `--map` type: _path | No argument help text is declared; parser destination is `map`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

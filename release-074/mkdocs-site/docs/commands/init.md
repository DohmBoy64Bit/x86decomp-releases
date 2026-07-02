---
title: x86decomp init
description: initialize a native PE project
original_path: commands/init.html
---

<a id="command-init"></a>

Section: Command reference

# `x86decomp init`

initialize a native PE project

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp init --help
```

Metadata: current · core

## `x86decomp init`

initialize a native PE project

### Usage

```
x86decomp init [-h] [--reference-binary] binary project
```

### Syntax example

```
x86decomp init ./target.exe ./work
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `binary` required · type: _path | No argument help text is declared; parser destination is `binary`. |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--reference-binary` nargs: 0 · default: False | No argument help text is declared; parser destination is `reference_binary`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

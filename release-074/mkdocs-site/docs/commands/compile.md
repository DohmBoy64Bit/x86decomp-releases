---
title: x86decomp compile
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/compile.html
---

<a id="command-compile"></a>

Section: Command reference

# `x86decomp compile`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp compile --help
```

Metadata: current · core

## `x86decomp compile`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp compile [-h] [--report REPORT] [--extra-arg EXTRA_ARG]
                         [--cache CACHE]
                         profile source output
```

### Syntax example

```
x86decomp compile ./input.json ./candidate.c ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `profile` required · type: _path | No argument help text is declared; parser destination is `profile`. |
| `source` required · type: _path | No argument help text is declared; parser destination is `source`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |
| `--extra-arg` default: [] | No argument help text is declared; parser destination is `extra_arg`. |
| `--cache` type: _path | No argument help text is declared; parser destination is `cache`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

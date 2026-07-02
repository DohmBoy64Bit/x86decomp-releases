---
title: x86decomp drcov-run
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/drcov-run.html
---

<a id="command-drcov-run"></a>

Section: Command reference

# `x86decomp drcov-run`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp drcov-run --help
```

Metadata: current · core

## `x86decomp drcov-run`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp drcov-run [-h] [--drrun DRRUN] [--program-arg PROGRAM_ARG]
                           [--timeout TIMEOUT] [--report REPORT]
                           executable output_directory
```

### Syntax example

```
x86decomp drcov-run ./target.exe ./output
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `executable` required · type: _path | No argument help text is declared; parser destination is `executable`. |
| `output_directory` required · type: _path | No argument help text is declared; parser destination is `output_directory`. |
| `--drrun` type: _path | No argument help text is declared; parser destination is `drrun`. |
| `--program-arg` default: [] | No argument help text is declared; parser destination is `program_arg`. |
| `--timeout` default: 300 · type: int | No argument help text is declared; parser destination is `timeout`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

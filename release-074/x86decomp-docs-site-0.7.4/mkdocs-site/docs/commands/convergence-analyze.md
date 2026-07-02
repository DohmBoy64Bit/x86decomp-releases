---
title: x86decomp convergence-analyze
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/convergence-analyze.html
---

<a id="command-convergence-analyze"></a>

Section: Command reference

# `x86decomp convergence-analyze`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp convergence-analyze --help
```

Metadata: current · core

## `x86decomp convergence-analyze`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp convergence-analyze [-h] [--profile PROFILE]
                                     [--previous PREVIOUS] [--report REPORT]
                                     [--history HISTORY]
                                     reference candidate
```

### Syntax example

```
x86decomp convergence-analyze ./reference.exe ./candidate.bin
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `reference` required · type: _path | No argument help text is declared; parser destination is `reference`. |
| `candidate` required · type: _path | No argument help text is declared; parser destination is `candidate`. |
| `--profile` type: _path | No argument help text is declared; parser destination is `profile`. |
| `--previous` type: _path | No argument help text is declared; parser destination is `previous`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |
| `--history` type: _path | No argument help text is declared; parser destination is `history`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

---
title: x86decomp symbolic-memory-validate
description: angr comparison with symbolic region bases and alias constraints
original_path: commands/symbolic-memory-validate.html
---

<a id="command-symbolic-memory-validate"></a>

Section: Command reference

# `x86decomp symbolic-memory-validate`

angr comparison with symbolic region bases and alias constraints

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp symbolic-memory-validate --help
```

Metadata: current · core

## `x86decomp symbolic-memory-validate`

angr comparison with symbolic region bases and alias constraints

### Usage

```
x86decomp symbolic-memory-validate [-h] [--report REPORT]
                                          target candidate harness
```

### Syntax example

```
x86decomp symbolic-memory-validate ./target.exe ./candidate.bin example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `target` required · type: _path | No argument help text is declared; parser destination is `target`. |
| `candidate` required · type: _path | No argument help text is declared; parser destination is `candidate`. |
| `harness` required · type: _path | No argument help text is declared; parser destination is `harness`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

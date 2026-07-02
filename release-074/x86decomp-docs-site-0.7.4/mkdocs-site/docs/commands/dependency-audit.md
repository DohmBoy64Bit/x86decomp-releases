---
title: x86decomp dependency-audit
description: run an installed pip-audit adapter and preserve exact findings
original_path: commands/dependency-audit.html
---

<a id="command-dependency-audit"></a>

Section: Command reference

# `x86decomp dependency-audit`

run an installed pip-audit adapter and preserve exact findings

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp dependency-audit --help
```

Metadata: current · core

## `x86decomp dependency-audit`

run an installed pip-audit adapter and preserve exact findings

### Usage

```
x86decomp dependency-audit [-h] [--executable EXECUTABLE]
                                  [--timeout TIMEOUT] [--report REPORT]
```

### Syntax example

```
x86decomp dependency-audit
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--executable` default: 'pip-audit' | No argument help text is declared; parser destination is `executable`. |
| `--timeout` default: 300 · type: int | No argument help text is declared; parser destination is `timeout`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

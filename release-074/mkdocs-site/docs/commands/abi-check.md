---
title: x86decomp abi-check
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/abi-check.html
---

<a id="command-abi-check"></a>

Section: Command reference

# `x86decomp abi-check`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp abi-check --help
```

Metadata: current · core

## `x86decomp abi-check`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp abi-check [-h] [--base BASE] [--report REPORT] code contract
```

### Syntax example

```
x86decomp abi-check ./function.bin ./contract.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `code` required · type: _path | No argument help text is declared; parser destination is `code`. |
| `contract` required · type: _path | No argument help text is declared; parser destination is `contract`. |
| `--base` default: 0 · type: _int | No argument help text is declared; parser destination is `base`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

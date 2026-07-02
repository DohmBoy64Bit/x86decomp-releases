---
title: x86decomp toolchain-register
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/toolchain-register.html
---

<a id="command-toolchain-register"></a>

Section: Command reference

# `x86decomp toolchain-register`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp toolchain-register --help
```

Metadata: current · core

## `x86decomp toolchain-register`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp toolchain-register [-h] --executable EXECUTABLE
                                    registry toolchain_id family version
```

### Syntax example

```
x86decomp toolchain-register example example-001 example example --executable ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `registry` required · type: _path | No argument help text is declared; parser destination is `registry`. |
| `toolchain_id` required | No argument help text is declared; parser destination is `toolchain_id`. |
| `family` required | No argument help text is declared; parser destination is `family`. |
| `version` required | No argument help text is declared; parser destination is `version`. |
| `--executable` required | role=path |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

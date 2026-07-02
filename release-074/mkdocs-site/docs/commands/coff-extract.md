---
title: x86decomp coff-extract
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/coff-extract.html
---

<a id="command-coff-extract"></a>

Section: Command reference

# `x86decomp coff-extract`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp coff-extract --help
```

Metadata: current · core

## `x86decomp coff-extract`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp coff-extract [-h] [--size SIZE] object symbol output
```

### Syntax example

```
x86decomp coff-extract ./candidate.obj example ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `object` required · type: _path | No argument help text is declared; parser destination is `object`. |
| `symbol` required | No argument help text is declared; parser destination is `symbol`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--size` type: _int | No argument help text is declared; parser destination is `size`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

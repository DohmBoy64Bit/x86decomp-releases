---
title: x86decomp serve
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/serve.html
---

<a id="command-serve"></a>

Section: Command reference

# `x86decomp serve`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp serve --help
```

Metadata: current · core

## `x86decomp serve`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp serve [-h] [--host HOST] [--port PORT] project
```

### Syntax example

```
x86decomp serve ./work
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--host` default: '127.0.0.1' | No argument help text is declared; parser destination is `host`. |
| `--port` default: 8765 · type: int | No argument help text is declared; parser destination is `port`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

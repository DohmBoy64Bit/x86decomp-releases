---
title: x86decomp coff-synthesize
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/coff-synthesize.html
---

<a id="command-coff-synthesize"></a>

Section: Command reference

# `x86decomp coff-synthesize`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp coff-synthesize --help
```

Metadata: current · core

## `x86decomp coff-synthesize`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}]
                                 [--relocations RELOCATIONS]
                                 code symbol output
```

### Syntax example

```
x86decomp coff-synthesize ./function.bin example ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `code` required · type: _path | No argument help text is declared; parser destination is `code`. |
| `symbol` required | No argument help text is declared; parser destination is `symbol`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |
| `--relocations` type: _path | No argument help text is declared; parser destination is `relocations`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

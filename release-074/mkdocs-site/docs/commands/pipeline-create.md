---
title: x86decomp pipeline-create
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/pipeline-create.html
---

<a id="command-pipeline-create"></a>

Section: Command reference

# `x86decomp pipeline-create`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp pipeline-create --help
```

Metadata: current · core

## `x86decomp pipeline-create`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp pipeline-create [-h] [--without-ghidra] project output
```

### Syntax example

```
x86decomp pipeline-create ./work ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--without-ghidra` nargs: 0 · default: False | No argument help text is declared; parser destination is `without_ghidra`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

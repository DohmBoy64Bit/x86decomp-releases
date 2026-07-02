---
title: x86decomp reproduce-create
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/reproduce-create.html
---

<a id="command-reproduce-create"></a>

Section: Command reference

# `x86decomp reproduce-create`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp reproduce-create --help
```

Metadata: current · core

## `x86decomp reproduce-create`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp reproduce-create [-h] [--required-tool REQUIRED_TOOL]
                                  project output
```

### Syntax example

```
x86decomp reproduce-create ./work ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--required-tool` | No argument help text is declared; parser destination is `required_tool`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

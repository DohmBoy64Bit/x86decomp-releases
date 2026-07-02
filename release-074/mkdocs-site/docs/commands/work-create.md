---
title: x86decomp work-create
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/work-create.html
---

<a id="command-work-create"></a>

Section: Command reference

# `x86decomp work-create`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp work-create --help
```

Metadata: current · core

## `x86decomp work-create`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY]
                             database function_id {matching,functional} kind
                             instructions
```

### Syntax example

```
x86decomp work-create ./analysis.db pe-rva:00001000 matching analysis example --validator example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `function_id` required | No argument help text is declared; parser destination is `function_id`. |
| `mode` required · choices: matching, functional | No argument help text is declared; parser destination is `mode`. |
| `kind` required | No argument help text is declared; parser destination is `kind`. |
| `instructions` required | No argument help text is declared; parser destination is `instructions`. |
| `--validator` required | No argument help text is declared; parser destination is `validator`. |
| `--priority` default: 0 · type: int | No argument help text is declared; parser destination is `priority`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

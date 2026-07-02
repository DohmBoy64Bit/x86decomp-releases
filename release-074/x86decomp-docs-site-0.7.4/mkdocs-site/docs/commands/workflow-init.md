---
title: x86decomp workflow-init
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/workflow-init.html
---

<a id="command-workflow-init"></a>

Section: Command reference

# `x86decomp workflow-init`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp workflow-init --help
```

Metadata: current · core

## `x86decomp workflow-init`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp workflow-init [-h] [--mode {matching,functional}]
                               project function_id
```

### Syntax example

```
x86decomp workflow-init ./work pe-rva:00001000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `function_id` required | No argument help text is declared; parser destination is `function_id`. |
| `--mode` choices: matching, functional | No argument help text is declared; parser destination is `mode`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

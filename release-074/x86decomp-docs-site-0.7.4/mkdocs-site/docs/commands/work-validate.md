---
title: x86decomp work-validate
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/work-validate.html
---

<a id="command-work-validate"></a>

Section: Command reference

# `x86decomp work-validate`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp work-validate --help
```

Metadata: current · core

## `x86decomp work-validate`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp work-validate [-h] [--passed]
                               database task_id validator report_path
```

### Syntax example

```
x86decomp work-validate ./analysis.db example-001 example-001 ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `task_id` required | No argument help text is declared; parser destination is `task_id`. |
| `validator` required | No argument help text is declared; parser destination is `validator`. |
| `report_path` required | No argument help text is declared; parser destination is `report_path`. |
| `--passed` nargs: 0 · default: False | No argument help text is declared; parser destination is `passed`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

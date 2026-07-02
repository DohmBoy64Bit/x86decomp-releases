---
title: x86decomp work-propose
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/work-propose.html
---

<a id="command-work-propose"></a>

Section: Command reference

# `x86decomp work-propose`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp work-propose --help
```

Metadata: current · core

## `x86decomp work-propose`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp work-propose [-h] --evidence EVIDENCE
                              database task_id proposal
```

### Syntax example

```
x86decomp work-propose ./analysis.db example-001 example --evidence example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `task_id` required | No argument help text is declared; parser destination is `task_id`. |
| `proposal` required · type: _path | No argument help text is declared; parser destination is `proposal`. |
| `--evidence` required | No argument help text is declared; parser destination is `evidence`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

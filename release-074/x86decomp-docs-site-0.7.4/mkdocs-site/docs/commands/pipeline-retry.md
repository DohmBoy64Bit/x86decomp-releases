---
title: x86decomp pipeline-retry
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/pipeline-retry.html
---

<a id="command-pipeline-retry"></a>

Section: Command reference

# `x86decomp pipeline-retry`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp pipeline-retry --help
```

Metadata: current · core

## `x86decomp pipeline-retry`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp pipeline-retry [-h] [--cascade] project pipeline_id stage_id
```

### Syntax example

```
x86decomp pipeline-retry ./work ./target.exe example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `pipeline_id` required | No argument help text is declared; parser destination is `pipeline_id`. |
| `stage_id` required | No argument help text is declared; parser destination is `stage_id`. |
| `--cascade` nargs: 0 · default: False | No argument help text is declared; parser destination is `cascade`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

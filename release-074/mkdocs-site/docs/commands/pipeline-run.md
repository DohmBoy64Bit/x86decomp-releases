---
title: x86decomp pipeline-run
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/pipeline-run.html
---

<a id="command-pipeline-run"></a>

Section: Command reference

# `x86decomp pipeline-run`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp pipeline-run --help
```

Metadata: current · core

## `x86decomp pipeline-run`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp pipeline-run [-h] [--continue-on-failure] project manifest
```

### Syntax example

```
x86decomp pipeline-run ./work ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `manifest` required · type: _path | No argument help text is declared; parser destination is `manifest`. |
| `--continue-on-failure` nargs: 0 · default: False | No argument help text is declared; parser destination is `continue_on_failure`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

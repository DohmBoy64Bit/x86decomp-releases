---
title: x86decomp integration-run
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/integration-run.html
---

<a id="command-integration-run"></a>

Section: Command reference

# `x86decomp integration-run`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp integration-run --help
```

Metadata: current · core

## `x86decomp integration-run`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp integration-run [-h] [--allow-host-execution]
                                 [--report REPORT]
                                 manifest
```

### Syntax example

```
x86decomp integration-run ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `manifest` required · type: _path | No argument help text is declared; parser destination is `manifest`. |
| `--allow-host-execution` nargs: 0 · default: False | No argument help text is declared; parser destination is `allow_host_execution`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

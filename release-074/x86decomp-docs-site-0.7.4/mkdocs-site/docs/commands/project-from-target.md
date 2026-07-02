---
title: x86decomp project-from-target
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/project-from-target.html
---

<a id="command-project-from-target"></a>

Section: Command reference

# `x86decomp project-from-target`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp project-from-target --help
```

Metadata: current · core

## `x86decomp project-from-target`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp project-from-target [-h] [--reference-binary]
                                     target_pack project
```

### Syntax example

```
x86decomp project-from-target ./target.exe ./work
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `target_pack` required · type: _path | No argument help text is declared; parser destination is `target_pack`. |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--reference-binary` nargs: 0 · default: False | No argument help text is declared; parser destination is `reference_binary`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

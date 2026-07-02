---
title: x86decomp memory-add
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/memory-add.html
---

<a id="command-memory-add"></a>

Section: Command reference

# `x86decomp memory-add`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp memory-add --help
```

Metadata: current · core

## `x86decomp memory-add`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp memory-add [-h] --actor ACTOR --category CATEGORY
                            --summary SUMMARY [--details-json DETAILS_JSON]
                            [--evidence EVIDENCE]
                            project
```

### Syntax example

```
x86decomp memory-add ./work --actor example --category example --summary example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--actor` required | No argument help text is declared; parser destination is `actor`. |
| `--category` required | No argument help text is declared; parser destination is `category`. |
| `--summary` required | No argument help text is declared; parser destination is `summary`. |
| `--details-json` default: '{}' | No argument help text is declared; parser destination is `details_json`. |
| `--evidence` default: [] | No argument help text is declared; parser destination is `evidence`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

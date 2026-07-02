---
title: x86decomp diff-bytes
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/diff-bytes.html
---

<a id="command-diff-bytes"></a>

Section: Command reference

# `x86decomp diff-bytes`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp diff-bytes --help
```

Metadata: current · core

## `x86decomp diff-bytes`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp diff-bytes [-h] [--report REPORT]
                            [--max-mismatches MAX_MISMATCHES]
                            target candidate
```

### Syntax example

```
x86decomp diff-bytes ./target.exe ./candidate.bin
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `target` required · type: _path | No argument help text is declared; parser destination is `target`. |
| `candidate` required · type: _path | No argument help text is declared; parser destination is `candidate`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |
| `--max-mismatches` default: 64 · type: int | No argument help text is declared; parser destination is `max_mismatches`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

---
title: x86decomp image-match
description: compare complete PE images under an explicit layout profile
original_path: commands/image-match.html
---

<a id="command-image-match"></a>

Section: Command reference

# `x86decomp image-match`

compare complete PE images under an explicit layout profile

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp image-match --help
```

Metadata: current · core

## `x86decomp image-match`

compare complete PE images under an explicit layout profile

### Usage

```
x86decomp image-match [-h] [--profile PROFILE] [--report REPORT]
                             reference candidate
```

### Syntax example

```
x86decomp image-match ./reference.exe ./candidate.bin
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `reference` required · type: _path | No argument help text is declared; parser destination is `reference`. |
| `candidate` required · type: _path | No argument help text is declared; parser destination is `candidate`. |
| `--profile` type: _path | No argument help text is declared; parser destination is `profile`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

---
title: x86decomp corpus-verify
description: verify source and output hashes in a ground-truth corpus
original_path: commands/corpus-verify.html
---

<a id="command-corpus-verify"></a>

Section: Command reference

# `x86decomp corpus-verify`

verify source and output hashes in a ground-truth corpus

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp corpus-verify --help
```

Metadata: current · core

## `x86decomp corpus-verify`

verify source and output hashes in a ground-truth corpus

### Usage

```
x86decomp corpus-verify [-h] report
```

### Syntax example

```
x86decomp corpus-verify ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `report` required · type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

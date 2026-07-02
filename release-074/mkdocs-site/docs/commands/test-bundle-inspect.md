---
title: x86decomp test-bundle-inspect
description: safely extract, verify, and statically inspect an authorized test bundle
original_path: commands/test-bundle-inspect.html
---

<a id="command-test-bundle-inspect"></a>

Section: Command reference

# `x86decomp test-bundle-inspect`

safely extract, verify, and statically inspect an authorized test bundle

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp test-bundle-inspect --help
```

Metadata: current · core

## `x86decomp test-bundle-inspect`

safely extract, verify, and statically inspect an authorized test bundle

### Usage

```
x86decomp test-bundle-inspect [-h] [--report REPORT] bundle
```

### Syntax example

```
x86decomp test-bundle-inspect example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `bundle` required · type: _path | No argument help text is declared; parser destination is `bundle`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

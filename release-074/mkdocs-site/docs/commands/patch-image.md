---
title: x86decomp patch-image
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/patch-image.html
---

<a id="command-patch-image"></a>

Section: Command reference

# `x86decomp patch-image`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp patch-image --help
```

Metadata: current · core

## `x86decomp patch-image`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp patch-image [-h] --rva RVA
                             [--expected-original-sha256 EXPECTED_ORIGINAL_SHA256]
                             [--expected-function-sha256 EXPECTED_FUNCTION_SHA256]
                             [--report REPORT]
                             original candidate output
```

### Syntax example

```
x86decomp patch-image ./original.bin ./candidate.bin ./output.json --rva 0x1000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `original` required · type: _path | No argument help text is declared; parser destination is `original`. |
| `candidate` required · type: _path | No argument help text is declared; parser destination is `candidate`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--rva` required · type: _int | No argument help text is declared; parser destination is `rva`. |
| `--expected-original-sha256` | No argument help text is declared; parser destination is `expected_original_sha256`. |
| `--expected-function-sha256` | No argument help text is declared; parser destination is `expected_function_sha256`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

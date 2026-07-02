---
title: x86decomp db-ingest
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/db-ingest.html
---

<a id="command-db-ingest"></a>

Section: Command reference

# `x86decomp db-ingest`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp db-ingest --help
```

Metadata: current · core

## `x86decomp db-ingest`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp db-ingest [-h] [--image-base IMAGE_BASE] database artifact
```

### Syntax example

```
x86decomp db-ingest ./analysis.db example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `artifact` required · type: _path | No argument help text is declared; parser destination is `artifact`. |
| `--image-base` default: 0 · type: _int | No argument help text is declared; parser destination is `image_base`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

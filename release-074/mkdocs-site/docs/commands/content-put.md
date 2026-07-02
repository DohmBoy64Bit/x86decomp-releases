---
title: x86decomp content-put
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/content-put.html
---

<a id="command-content-put"></a>

Section: Command reference

# `x86decomp content-put`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp content-put --help
```

Metadata: current · core

## `x86decomp content-put`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp content-put [-h] [--media-type MEDIA_TYPE]
                             [--reference REFERENCE] [--kind KIND]
                             [--owner OWNER]
                             store file
```

### Syntax example

```
x86decomp content-put example ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `store` required · type: _path | No argument help text is declared; parser destination is `store`. |
| `file` required · type: _path | No argument help text is declared; parser destination is `file`. |
| `--media-type` default: 'application/octet-stream' | No argument help text is declared; parser destination is `media_type`. |
| `--reference` | No argument help text is declared; parser destination is `reference`. |
| `--kind` default: 'artifact' | No argument help text is declared; parser destination is `kind`. |
| `--owner` default: 'user' | No argument help text is declared; parser destination is `owner`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

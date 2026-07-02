---
title: x86decomp image-profile
description: derive a target-specific whole-image profile
original_path: commands/image-profile.html
---

<a id="command-image-profile"></a>

Section: Command reference

# `x86decomp image-profile`

derive a target-specific whole-image profile

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp image-profile --help
```

Metadata: current · core

## `x86decomp image-profile`

derive a target-specific whole-image profile

### Usage

```
x86decomp image-profile [-h] reference output
```

### Syntax example

```
x86decomp image-profile ./reference.exe ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `reference` required · type: _path | No argument help text is declared; parser destination is `reference`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

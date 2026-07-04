---
title: x86decomp reloc
description: Command reference for `x86decomp reloc`.
---


# `x86decomp reloc`

Canonical reloc commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp reloc [-h] [--project PROJECT] [--actor ACTOR]
                       {inspect,resolve,supported} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `inspect` | `usage: x86decomp reloc inspect [-h] [--symbol SYMBOL] object` | `assembly` |
| `resolve` | `usage: x86decomp reloc resolve [-h] [--image-base IMAGE_BASE] object symbol base_rva symbol_map output` | `assembly` |
| `supported` | `usage: x86decomp reloc supported [-h]` | `assembly` |

### `x86decomp reloc inspect`

```text
usage: x86decomp reloc inspect [-h] [--symbol SYMBOL] object
```

| Argument | Details |
| --- | --- |
| `object` | required. |
| `--symbol` | — |

### `x86decomp reloc resolve`

```text
usage: x86decomp reloc resolve [-h] [--image-base IMAGE_BASE]
                               object symbol base_rva symbol_map output
```

| Argument | Details |
| --- | --- |
| `object` | required. |
| `symbol` | required. |
| `base_rva` | required · type: `int`. |
| `symbol_map` | required. |
| `output` | required. |
| `--image-base` | type: `int` · default: `0`. |

### `x86decomp reloc supported`

```text
usage: x86decomp reloc supported [-h]
```



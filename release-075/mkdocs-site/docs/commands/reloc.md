---
title: x86decomp reloc
description: Exact parser-derived reference for x86decomp reloc in 0.7.5.
---

# `x86decomp reloc`

Canonical capability group with 3 routes. Shared group options are shown in every exact usage string.

## `x86decomp reloc inspect`

usage: x86decomp reloc inspect [-h] [--symbol SYMBOL] object

### Usage

```text
x86decomp reloc inspect [-h] [--symbol SYMBOL] object
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `object` | required. No help text is declared; parser destination is `object`. |
| `--symbol` | declared. No help text is declared; parser destination is `symbol`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp reloc resolve`

usage: x86decomp reloc resolve [-h] [--image-base IMAGE_BASE]

### Usage

```text
x86decomp reloc resolve [-h] [--image-base IMAGE_BASE]
                               object symbol base_rva symbol_map output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `object` | required. No help text is declared; parser destination is `object`. |
| `symbol` | required. No help text is declared; parser destination is `symbol`. |
| `base_rva` | required · type: `_int`. No help text is declared; parser destination is `base_rva`. |
| `symbol_map` | required. No help text is declared; parser destination is `symbol_map`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--image-base` | default: `0` · type: `_int`. No help text is declared; parser destination is `image_base`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp reloc supported`

usage: x86decomp reloc supported [-h]

### Usage

```text
x86decomp reloc supported [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |

---
title: x86decomp reloc
description: Exact v0.7.8 parser-derived reference for `x86decomp reloc`.
---


# `x86decomp reloc`

Canonical reloc commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp reloc [-h] [--project PROJECT] [--actor ACTOR]
                       {inspect,resolve,supported} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `object` | required · parser destination: `object`. No help text declared. |
| `--symbol` | parser destination: `symbol`. No help text declared. |

### `x86decomp reloc resolve`

```text
usage: x86decomp reloc resolve [-h] [--image-base IMAGE_BASE]
                               object symbol base_rva symbol_map output
```

| Argument | Exact parser declaration |
| --- | --- |
| `object` | required · parser destination: `object`. No help text declared. |
| `symbol` | required · parser destination: `symbol`. No help text declared. |
| `base_rva` | required · type: `_int` · parser destination: `base_rva`. No help text declared. |
| `symbol_map` | required · parser destination: `symbol_map`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--image-base` | type: `_int` · default: `0` · parser destination: `image_base`. No help text declared. |

### `x86decomp reloc supported`

```text
usage: x86decomp reloc supported [-h]
```

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| assembly cli | `src/x86decomp/assembly/cli.py` | `6c8a227f8c1a9c48a83e1f048f6160f8740e97552fa6967dea122f42fab45f88` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

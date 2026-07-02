---
title: x86decomp reloc
description: Canonical reloc commands implemented by the current capability subsystem.
original_path: commands/reloc.html
---

<a id="command-reloc-inspect"></a>
<a id="command-reloc-resolve"></a>
<a id="command-reloc-supported"></a>

Section: Command reference

# `x86decomp reloc`

Canonical reloc commands implemented by the current capability subsystem.

Metadata: current · canonical group · 3 runnable paths

## Help

```
x86decomp reloc --help
```

Metadata: current · assembly

## `x86decomp reloc inspect`

inspect command

### Usage

```
x86decomp reloc inspect [-h] [--symbol SYMBOL] object
```

### Syntax example

```
x86decomp reloc inspect ./candidate.obj
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `object` required | No argument help text is declared; parser destination is `object`. |
| `--symbol` | No argument help text is declared; parser destination is `symbol`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp reloc resolve`

resolve command

### Usage

```
x86decomp reloc resolve [-h] [--image-base IMAGE_BASE]
                               object symbol base_rva symbol_map output
```

### Syntax example

```
x86decomp reloc resolve ./candidate.obj example 0x400000 ./target.map ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `object` required | No argument help text is declared; parser destination is `object`. |
| `symbol` required | No argument help text is declared; parser destination is `symbol`. |
| `base_rva` required · type: _int | No argument help text is declared; parser destination is `base_rva`. |
| `symbol_map` required | No argument help text is declared; parser destination is `symbol_map`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--image-base` default: 0 · type: _int | No argument help text is declared; parser destination is `image_base`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp reloc supported`

supported command

### Usage

```
x86decomp reloc supported [-h]
```

### Syntax example

```
x86decomp reloc supported
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

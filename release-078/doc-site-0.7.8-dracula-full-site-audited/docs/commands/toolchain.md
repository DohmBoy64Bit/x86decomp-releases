---
title: x86decomp toolchain
description: Exact v0.7.8 parser-derived reference for `x86decomp toolchain`.
---


# `x86decomp toolchain`

Canonical toolchain commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp toolchain [-h] [--project PROJECT] [--actor ACTOR]
                           {hash-tree,redact-package,verify-local} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `hash-tree` | `usage: x86decomp toolchain hash-tree [-h] root output` | `reconstruction` |
| `redact-package` | `usage: x86decomp toolchain redact-package [-h] [--manifest MANIFEST] root output` | `reconstruction` |
| `verify-local` | `usage: x86decomp toolchain verify-local [-h] [--output OUTPUT] manifest` | `reconstruction` |

### `x86decomp toolchain hash-tree`

```text
usage: x86decomp toolchain hash-tree [-h] root output
```

| Argument | Exact parser declaration |
| --- | --- |
| `root` | required · parser destination: `root`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp toolchain redact-package`

```text
usage: x86decomp toolchain redact-package [-h] [--manifest MANIFEST]
                                          root output
```

| Argument | Exact parser declaration |
| --- | --- |
| `root` | required · parser destination: `root`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--manifest` | parser destination: `manifest`. No help text declared. |

### `x86decomp toolchain verify-local`

```text
usage: x86decomp toolchain verify-local [-h] [--output OUTPUT] manifest
```

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required · parser destination: `manifest`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

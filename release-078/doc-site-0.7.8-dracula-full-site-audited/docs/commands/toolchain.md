---
title: x86decomp toolchain
description: Command reference for `x86decomp toolchain`.
---


# `x86decomp toolchain`

Canonical toolchain commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp toolchain [-h] [--project PROJECT] [--actor ACTOR]
                           {hash-tree,redact-package,verify-local} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

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

| Argument | Details |
| --- | --- |
| `root` | required. |
| `output` | required. |

### `x86decomp toolchain redact-package`

```text
usage: x86decomp toolchain redact-package [-h] [--manifest MANIFEST]
                                          root output
```

| Argument | Details |
| --- | --- |
| `root` | required. |
| `output` | required. |
| `--manifest` | — |

### `x86decomp toolchain verify-local`

```text
usage: x86decomp toolchain verify-local [-h] [--output OUTPUT] manifest
```

| Argument | Details |
| --- | --- |
| `manifest` | required. |
| `--output` | — |



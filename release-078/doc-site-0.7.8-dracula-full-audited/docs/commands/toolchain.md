---
title: x86decomp toolchain
---

# `x86decomp toolchain`

Canonical toolchain commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp toolchain [-h] [--project PROJECT] [--actor ACTOR]
                           {hash-tree,redact-package,verify-local} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `hash-tree` | `usage: x86decomp toolchain hash-tree [-h] root output` |
| `redact-package` | `usage: x86decomp toolchain redact-package [-h] [--manifest MANIFEST] root output` |
| `verify-local` | `usage: x86decomp toolchain verify-local [-h] [--output OUTPUT] manifest` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp toolchain hash-tree` | `reconstruction` |
| `x86decomp toolchain redact-package` | `reconstruction` |
| `x86decomp toolchain verify-local` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.

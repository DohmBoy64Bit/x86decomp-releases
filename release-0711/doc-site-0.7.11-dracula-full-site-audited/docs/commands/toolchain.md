---
title: x86decomp toolchain
description: Parser-derived command reference page for `toolchain`.
---

# `x86decomp toolchain`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `hash-tree` | `reconstruction` |
| `redact-package` | `reconstruction` |
| `verify-local` | `reconstruction` |
## Parser help

```text
usage: x86decomp toolchain [-h] [--project PROJECT] [--actor ACTOR]
                           {hash-tree,redact-package,verify-local} ...

Canonical toolchain commands implemented by the current capability subsystem.

positional arguments:
  {hash-tree,redact-package,verify-local}
    hash-tree           hash-tree command
    redact-package      redact-package command
    verify-local        verify-local command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

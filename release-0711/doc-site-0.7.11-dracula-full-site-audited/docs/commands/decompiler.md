---
title: x86decomp decompiler
description: Parser-derived command reference page for `decompiler`.
---

# `x86decomp decompiler`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `cleanup` | `reconstruction` |
## Parser help

```text
usage: x86decomp decompiler [-h] [--project PROJECT] [--actor ACTOR]
                            {cleanup} ...

Canonical decompiler commands implemented by the current capability subsystem.

positional arguments:
  {cleanup}
    cleanup          cleanup command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

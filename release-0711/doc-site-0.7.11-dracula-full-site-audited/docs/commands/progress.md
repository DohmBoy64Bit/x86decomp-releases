---
title: x86decomp progress
description: Parser-derived command reference page for `progress`.
---

# `x86decomp progress`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `reconcile` | `reconstruction` |
## Parser help

```text
usage: x86decomp progress [-h] [--project PROJECT] [--actor ACTOR]
                          {reconcile} ...

Canonical progress commands implemented by the current capability subsystem.

positional arguments:
  {reconcile}
    reconcile        reconcile command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

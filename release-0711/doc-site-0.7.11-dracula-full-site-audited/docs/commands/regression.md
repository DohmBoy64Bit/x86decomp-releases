---
title: x86decomp regression
description: Parser-derived command reference page for `regression`.
---

# `x86decomp regression`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `compare` | `reconstruction` |
## Parser help

```text
usage: x86decomp regression [-h] [--project PROJECT] [--actor ACTOR]
                            {compare} ...

Canonical regression commands implemented by the current capability subsystem.

positional arguments:
  {compare}
    compare          compare command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

---
title: x86decomp subsystem
description: Parser-derived command reference page for `subsystem`.
---

# `x86decomp subsystem`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `detect` | `reconstruction` |
## Parser help

```text
usage: x86decomp subsystem [-h] [--project PROJECT] [--actor ACTOR]
                           {detect} ...

Canonical subsystem commands implemented by the current capability subsystem.

positional arguments:
  {detect}
    detect           detect command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

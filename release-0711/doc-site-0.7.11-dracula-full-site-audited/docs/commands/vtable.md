---
title: x86decomp vtable
description: Parser-derived command reference page for `vtable`.
---

# `x86decomp vtable`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `recover` | `reconstruction` |
## Parser help

```text
usage: x86decomp vtable [-h] [--project PROJECT] [--actor ACTOR] {recover} ...

Canonical vtable commands implemented by the current capability subsystem.

positional arguments:
  {recover}
    recover          recover command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

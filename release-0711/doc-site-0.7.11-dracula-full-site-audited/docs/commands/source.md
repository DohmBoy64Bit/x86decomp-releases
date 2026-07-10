---
title: x86decomp source
description: Parser-derived command reference page for `source`.
---

# `x86decomp source`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `impact` | `reconstruction` |
| `lock` | `reconstruction` |
| `reconcile` | `reconstruction` |
| `unlock` | `reconstruction` |
## Parser help

```text
usage: x86decomp source [-h] [--project PROJECT] [--actor ACTOR]
                        {impact,lock,reconcile,unlock} ...

Canonical source commands implemented by the current capability subsystem.

positional arguments:
  {impact,lock,reconcile,unlock}
    impact              impact command
    lock                lock command
    reconcile           reconcile command
    unlock              unlock command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

---
title: x86decomp function
description: Parser-derived command reference page for `function`.
---

# `x86decomp function`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `classify` | `reconstruction` |
| `discover` | `reconstruction` |
| `reconcile` | `reconstruction` |
| `sort` | `reconstruction` |
## Parser help

```text
usage: x86decomp function [-h] [--project PROJECT] [--actor ACTOR]
                          {classify,discover,reconcile,sort} ...

Canonical function commands implemented by the current capability subsystem.

positional arguments:
  {classify,discover,reconcile,sort}
    classify            classify command
    discover            discover command
    reconcile           reconcile command
    sort                sort command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

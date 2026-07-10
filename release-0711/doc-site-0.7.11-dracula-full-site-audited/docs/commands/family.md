---
title: x86decomp family
description: Parser-derived command reference page for `family`.
---

# `x86decomp family`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `add` | `governance` |
| `correlate` | `governance` |
| `create` | `governance` |
| `report` | `governance` |
## Parser help

```text
usage: x86decomp family [-h] [--project PROJECT] [--actor ACTOR]
                        {add,correlate,create,report} ...

Canonical family commands implemented by the current capability subsystem.

positional arguments:
  {add,correlate,create,report}
    add                 add command
    correlate           correlate command
    create              create command
    report              report command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

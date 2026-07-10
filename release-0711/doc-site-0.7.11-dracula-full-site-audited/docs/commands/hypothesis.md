---
title: x86decomp hypothesis
description: Parser-derived command reference page for `hypothesis`.
---

# `x86decomp hypothesis`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `create` | `governance` |
| `dependency` | `governance` |
| `evidence` | `governance` |
| `gate` | `governance` |
| `list` | `governance` |
| `show` | `governance` |
| `transition` | `governance` |
## Parser help

```text
usage: x86decomp hypothesis [-h] [--project PROJECT] [--actor ACTOR]
                            {create,dependency,evidence,gate,list,show,transition} ...

Canonical hypothesis commands implemented by the current capability subsystem.

positional arguments:
  {create,dependency,evidence,gate,list,show,transition}
    create              create command
    dependency          dependency command
    evidence            evidence command
    gate                gate command
    list                list command
    show                show command
    transition          transition command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

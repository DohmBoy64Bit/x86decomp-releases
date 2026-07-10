---
title: x86decomp candidate
description: Parser-derived command reference page for `candidate`.
---

# `x86decomp candidate`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `add-file` | `governance` |
| `compare` | `governance` |
| `create` | `governance` |
| `evaluate` | `governance` |
| `list` | `governance` |
| `promote` | `reconstruction` |
| `search` | `reconstruction` |
| `show` | `governance` |
| `transition` | `governance` |
## Parser help

```text
usage: x86decomp candidate [-h] [--project PROJECT] [--actor ACTOR]
                           {add-file,compare,create,evaluate,list,promote,search,show,transition} ...

Canonical candidate commands implemented by the current capability subsystem.

positional arguments:
  {add-file,compare,create,evaluate,list,promote,search,show,transition}
    add-file            add-file command
    compare             compare command
    create              create command
    evaluate            evaluate command
    list                list command
    promote             promote command
    search              emit an ordered candidate-search plan only; no source
                        edits or promotions are performed
    show                show command
    transition          transition command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

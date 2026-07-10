---
title: x86decomp build
description: Parser-derived command reference page for `build`.
---

# `x86decomp build`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `add-target` | `reconstruction` |
| `add-variant` | `reconstruction` |
| `compare-modes` | `reconstruction` |
| `create` | `reconstruction` |
| `generate` | `reconstruction` |
| `matrix` | `reconstruction` |
| `show` | `reconstruction` |
| `validate` | `reconstruction` |
## Parser help

```text
usage: x86decomp build [-h] [--project PROJECT] [--actor ACTOR]
                       {add-target,add-variant,compare-modes,create,generate,matrix,show,validate} ...

Canonical build commands implemented by the current capability subsystem.

positional arguments:
  {add-target,add-variant,compare-modes,create,generate,matrix,show,validate}
    add-target          add-target command
    add-variant         add-variant command
    compare-modes       compare-modes command
    create              create command
    generate            generate command
    matrix              matrix command
    show                show command
    validate            validate command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

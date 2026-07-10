---
title: x86decomp runtime
description: Parser-derived command reference page for `runtime`.
---

# `x86decomp runtime`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `launch` | `native` |
| `map-crash` | `native` |
| `validate-image` | `native` |
## Parser help

```text
usage: x86decomp runtime [-h] [--project PROJECT] [--actor ACTOR]
                         {launch,map-crash,validate-image} ...

Canonical runtime commands implemented by the current capability subsystem.

positional arguments:
  {launch,map-crash,validate-image}
    launch              launch command
    map-crash           map-crash command
    validate-image      validate-image command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

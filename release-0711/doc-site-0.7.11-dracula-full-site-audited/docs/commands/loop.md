---
title: x86decomp loop
description: Parser-derived command reference page for `loop`.
---

# `x86decomp loop`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `list` | `native` |
| `run` | `native` |
| `show` | `native` |
## Parser help

```text
usage: x86decomp loop [-h] [--project PROJECT] [--actor ACTOR]
                      {list,run,show} ...

Canonical loop commands implemented by the current capability subsystem.

positional arguments:
  {list,run,show}
    list             list command
    run              run command
    show             show command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

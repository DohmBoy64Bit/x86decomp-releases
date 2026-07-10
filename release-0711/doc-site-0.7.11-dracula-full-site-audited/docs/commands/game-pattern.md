---
title: x86decomp game-pattern
description: Parser-derived command reference page for `game-pattern`.
---

# `x86decomp game-pattern`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `state-machine` | `reconstruction` |
## Parser help

```text
usage: x86decomp game-pattern [-h] [--project PROJECT] [--actor ACTOR]
                              {state-machine} ...

Canonical game-pattern commands implemented by the current capability
subsystem.

positional arguments:
  {state-machine}
    state-machine    state-machine command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

---
title: x86decomp graph
description: Parser-derived command reference page for `graph`.
---

# `x86decomp graph`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `edge` | `governance` |
| `impact` | `governance` |
| `node` | `governance` |
## Parser help

```text
usage: x86decomp graph [-h] [--project PROJECT] [--actor ACTOR]
                       {edge,impact,node} ...

Canonical graph commands implemented by the current capability subsystem.

positional arguments:
  {edge,impact,node}
    edge              edge command
    impact            impact command
    node              node command

options:
  -h, --help          show this help message and exit
  --project PROJECT   project root used by the capability implementation
                      (default: current directory)
  --actor ACTOR
```

---
title: x86decomp review
description: Parser-derived command reference page for `review`.
---

# `x86decomp review`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `assign` | `governance` |
| `create` | `governance` |
| `decide` | `governance` |
| `list` | `governance` |
| `lock` | `governance` |
| `show` | `governance` |
## Parser help

```text
usage: x86decomp review [-h] [--project PROJECT] [--actor ACTOR]
                        {assign,create,decide,list,lock,show} ...

Canonical review commands implemented by the current capability subsystem.

positional arguments:
  {assign,create,decide,list,lock,show}
    assign              assign command
    create              create command
    decide              decide command
    list                list command
    lock                lock command
    show                show command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

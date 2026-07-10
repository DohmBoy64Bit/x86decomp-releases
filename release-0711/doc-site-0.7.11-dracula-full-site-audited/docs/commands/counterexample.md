---
title: x86decomp counterexample
description: Parser-derived command reference page for `counterexample`.
---

# `x86decomp counterexample`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `add` | `governance` |
| `list` | `governance` |
| `promote` | `governance` |
| `show` | `governance` |
## Parser help

```text
usage: x86decomp counterexample [-h] [--project PROJECT] [--actor ACTOR]
                                {add,list,promote,show} ...

Canonical counterexample commands implemented by the current capability
subsystem.

positional arguments:
  {add,list,promote,show}
    add                 add command
    list                list command
    promote             promote command
    show                show command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

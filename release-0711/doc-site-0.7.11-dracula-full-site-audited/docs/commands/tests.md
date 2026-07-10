---
title: x86decomp tests
description: Parser-derived command reference page for `tests`.
---

# `x86decomp tests`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `add` | `reconstruction` |
| `explain` | `reconstruction` |
| `list` | `reconstruction` |
| `promote-counterexample` | `reconstruction` |
| `synthesize` | `reconstruction` |
## Parser help

```text
usage: x86decomp tests [-h] [--project PROJECT] [--actor ACTOR]
                       {add,explain,list,promote-counterexample,synthesize} ...

Canonical tests commands implemented by the current capability subsystem.

positional arguments:
  {add,explain,list,promote-counterexample,synthesize}
    add                 add command
    explain             explain command
    list                list command
    promote-counterexample
                        promote-counterexample command
    synthesize          synthesize command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

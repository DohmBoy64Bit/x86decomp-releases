---
title: x86decomp module
description: Parser-derived command reference page for `module`.
---

# `x86decomp module`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `add-member` | `reconstruction` |
| `add-unit-member` | `reconstruction` |
| `assign` | `reconstruction` |
| `create` | `reconstruction` |
| `create-unit` | `reconstruction` |
| `list` | `reconstruction` |
| `show` | `reconstruction` |
| `show-unit` | `reconstruction` |
| `suggest` | `reconstruction` |
## Parser help

```text
usage: x86decomp module [-h] [--project PROJECT] [--actor ACTOR]
                        {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest} ...

Canonical module commands implemented by the current capability subsystem.

positional arguments:
  {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest}
    add-member          add-member command
    add-unit-member     add-unit-member command
    assign              assign command
    create              create command
    create-unit         create-unit command
    list                list command
    show                show command
    show-unit           show-unit command
    suggest             suggest command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

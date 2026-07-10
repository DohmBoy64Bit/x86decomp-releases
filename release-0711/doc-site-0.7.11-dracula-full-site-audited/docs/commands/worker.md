---
title: x86decomp worker
description: Parser-derived command reference page for `worker`.
---

# `x86decomp worker`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `doctor` | `governance` |
| `list` | `governance` |
| `register` | `governance` |
| `select` | `governance` |
| `status` | `governance` |
## Parser help

```text
usage: x86decomp worker [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,list,register,select,status} ...

Canonical worker commands implemented by the current capability subsystem.

positional arguments:
  {doctor,list,register,select,status}
    doctor              doctor command
    list                list command
    register            register command
    select              select command
    status              status command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

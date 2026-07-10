---
title: x86decomp plugin
description: Parser-derived command reference page for `plugin`.
---

# `x86decomp plugin`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `doctor` | `governance` |
| `install` | `governance` |
| `invoke` | `governance` |
| `list` | `governance` |
| `validate` | `governance` |
## Parser help

```text
usage: x86decomp plugin [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,install,invoke,list,validate} ...

Canonical plugin commands implemented by the current capability subsystem.

positional arguments:
  {doctor,install,invoke,list,validate}
    doctor              doctor command
    install             install command
    invoke              invoke command
    list                list command
    validate            validate command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

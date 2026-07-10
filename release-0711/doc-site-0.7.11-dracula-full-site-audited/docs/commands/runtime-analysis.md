---
title: x86decomp runtime-analysis
description: Parser-derived command reference page for `runtime-analysis`.
---

# `x86decomp runtime-analysis`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `identify` | `reconstruction` |
| `match-library` | `reconstruction` |
| `quarantine` | `reconstruction` |
## Parser help

```text
usage: x86decomp runtime-analysis [-h] [--project PROJECT] [--actor ACTOR]
                                  {identify,match-library,quarantine} ...

Canonical runtime-analysis commands implemented by the current capability
subsystem.

positional arguments:
  {identify,match-library,quarantine}
    identify            identify command
    match-library       match-library command
    quarantine          quarantine command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

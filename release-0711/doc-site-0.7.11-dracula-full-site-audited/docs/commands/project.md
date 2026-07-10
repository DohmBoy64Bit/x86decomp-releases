---
title: x86decomp project
description: Parser-derived command reference page for `project`.
---

# `x86decomp project`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `check` | `assembly` |
| `doctor-paths` | `reconstruction` |
| `explain-boundaries` | `reconstruction` |
| `export` | `reconstruction` |
| `health` | `reconstruction` |
| `init` | `assembly` |
| `synthesize-layout` | `reconstruction` |
## Parser help

```text
usage: x86decomp project [-h] [--project PROJECT] [--actor ACTOR]
                         {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout} ...

Canonical project commands implemented by the current capability subsystem.

positional arguments:
  {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout}
    check               check command
    doctor-paths        doctor-paths command
    explain-boundaries  explain-boundaries command
    export              export command
    health              health command
    init                init command
    synthesize-layout   synthesize-layout command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

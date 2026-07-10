---
title: x86decomp proof
description: Parser-derived command reference page for `proof`.
---

# `x86decomp proof`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `evaluate` | `governance` |
| `export` | `governance` |
| `inspect` | `governance` |
| `obligation` | `governance` |
| `result` | `governance` |
| `verify` | `governance` |
## Parser help

```text
usage: x86decomp proof [-h] [--project PROJECT] [--actor ACTOR]
                       {evaluate,export,inspect,obligation,result,verify} ...

Canonical proof commands implemented by the current capability subsystem.

positional arguments:
  {evaluate,export,inspect,obligation,result,verify}
    evaluate            evaluate command
    export              export command
    inspect             inspect command
    obligation          obligation command
    result              result command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

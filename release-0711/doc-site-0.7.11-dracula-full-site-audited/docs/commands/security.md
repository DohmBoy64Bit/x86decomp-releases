---
title: x86decomp security
description: Parser-derived command reference page for `security`.
---

# `x86decomp security`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `finding` | `reconstruction` |
| `policy` | `reconstruction` |
| `report` | `reconstruction` |
| `scan` | `reconstruction` |
## Parser help

```text
usage: x86decomp security [-h] [--project PROJECT] [--actor ACTOR]
                          {finding,policy,report,scan} ...

Canonical security commands implemented by the current capability subsystem.

positional arguments:
  {finding,policy,report,scan}
    finding             finding command
    policy              policy command
    report              report command
    scan                scan command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

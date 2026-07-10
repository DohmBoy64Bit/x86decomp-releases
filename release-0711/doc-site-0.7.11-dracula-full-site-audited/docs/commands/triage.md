---
title: x86decomp triage
description: Parser-derived command reference page for `triage`.
---

# `x86decomp triage`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `next` | `reconstruction` |
## Parser help

```text
usage: x86decomp triage [-h] [--project PROJECT] [--actor ACTOR] {next} ...

Canonical triage commands implemented by the current capability subsystem.

positional arguments:
  {next}
    next             emit a triage plan only; no workflow state is modified

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

---
title: x86decomp compiler-rules
description: Parser-derived command reference page for `compiler-rules`.
---

# `x86decomp compiler-rules`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `compare-flags` | `reconstruction` |
| `learn-rule` | `reconstruction` |
| `rule-report` | `reconstruction` |
## Parser help

```text
usage: x86decomp compiler-rules [-h] [--project PROJECT] [--actor ACTOR]
                                {compare-flags,learn-rule,rule-report} ...

Canonical compiler-rules commands implemented by the current capability
subsystem.

positional arguments:
  {compare-flags,learn-rule,rule-report}
    compare-flags       compare-flags command
    learn-rule          learn-rule command
    rule-report         rule-report command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

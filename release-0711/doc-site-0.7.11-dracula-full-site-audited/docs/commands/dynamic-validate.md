---
title: x86decomp dynamic-validate
description: Parser-derived command reference page for `dynamic-validate`.
---

# `x86decomp dynamic-validate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp dynamic-validate [-h] [--target-base TARGET_BASE]
                                  [--candidate-base CANDIDATE_BASE]
                                  [--report REPORT]
                                  target candidate harness

positional arguments:
  target
  candidate
  harness

options:
  -h, --help            show this help message and exit
  --target-base TARGET_BASE
  --candidate-base CANDIDATE_BASE
  --report REPORT
```

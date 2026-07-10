---
title: x86decomp diff-bytes
description: Parser-derived command reference page for `diff-bytes`.
---

# `x86decomp diff-bytes`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp diff-bytes [-h] [--report REPORT]
                            [--max-mismatches MAX_MISMATCHES]
                            target candidate

positional arguments:
  target
  candidate

options:
  -h, --help            show this help message and exit
  --report REPORT
  --max-mismatches MAX_MISMATCHES
```

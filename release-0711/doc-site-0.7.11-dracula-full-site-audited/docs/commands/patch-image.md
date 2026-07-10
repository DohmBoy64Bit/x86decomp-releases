---
title: x86decomp patch-image
description: Parser-derived command reference page for `patch-image`.
---

# `x86decomp patch-image`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp patch-image [-h] --rva RVA
                             [--expected-original-sha256 EXPECTED_ORIGINAL_SHA256]
                             [--expected-function-sha256 EXPECTED_FUNCTION_SHA256]
                             [--report REPORT]
                             original candidate output

positional arguments:
  original
  candidate
  output

options:
  -h, --help            show this help message and exit
  --rva RVA
  --expected-original-sha256 EXPECTED_ORIGINAL_SHA256
  --expected-function-sha256 EXPECTED_FUNCTION_SHA256
  --report REPORT
```

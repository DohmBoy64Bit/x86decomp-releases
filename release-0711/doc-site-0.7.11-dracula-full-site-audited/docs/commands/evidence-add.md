---
title: x86decomp evidence-add
description: Parser-derived command reference page for `evidence-add`.
---

# `x86decomp evidence-add`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp evidence-add [-h]
                              --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
                              --source SOURCE --locator LOCATOR
                              --assertion ASSERTION
                              --independent-group INDEPENDENT_GROUP
                              [--file FILE] [--id ID]
                              project

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
  --source SOURCE
  --locator LOCATOR
  --assertion ASSERTION
  --independent-group INDEPENDENT_GROUP
  --file FILE
  --id ID
```

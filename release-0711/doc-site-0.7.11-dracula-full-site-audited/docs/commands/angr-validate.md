---
title: x86decomp angr-validate
description: Parser-derived command reference page for `angr-validate`.
---

# `x86decomp angr-validate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp angr-validate [-h] [--architecture {x86,x86_64}]
                               [--input-register INPUT_REGISTER]
                               [--stack-argument-words STACK_ARGUMENT_WORDS]
                               [--output-register OUTPUT_REGISTER]
                               [--max-steps MAX_STEPS] [--max-paths MAX_PATHS]
                               [--report REPORT]
                               target candidate

positional arguments:
  target
  candidate

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --input-register INPUT_REGISTER
  --stack-argument-words STACK_ARGUMENT_WORDS
  --output-register OUTPUT_REGISTER
  --max-steps MAX_STEPS
  --max-paths MAX_PATHS
  --report REPORT
```

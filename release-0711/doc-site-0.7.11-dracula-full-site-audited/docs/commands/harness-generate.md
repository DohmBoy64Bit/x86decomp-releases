---
title: x86decomp harness-generate
description: Parser-derived command reference page for `harness-generate`.
---

# `x86decomp harness-generate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp harness-generate [-h]
                                  [--pointer-parameters POINTER_PARAMETERS]
                                  [--no-observe-pointers]
                                  [--max-instructions MAX_INSTRUCTIONS]
                                  [--timeout-ms TIMEOUT_MS]
                                  abi_contract output

positional arguments:
  abi_contract
  output

options:
  -h, --help            show this help message and exit
  --pointer-parameters POINTER_PARAMETERS
  --no-observe-pointers
  --max-instructions MAX_INSTRUCTIONS
  --timeout-ms TIMEOUT_MS
```

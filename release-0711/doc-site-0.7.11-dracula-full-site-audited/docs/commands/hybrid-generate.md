---
title: x86decomp hybrid-generate
description: Parser-derived command reference page for `hybrid-generate`.
---

# `x86decomp hybrid-generate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp hybrid-generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 project output

positional arguments:
  project
  output

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --asm-format {bytes,annotated,mnemonic}
  --image-base IMAGE_BASE
  --assembler-command-json ASSEMBLER_COMMAND_JSON
  --symbol-map SYMBOL_MAP
  --overwrite
```

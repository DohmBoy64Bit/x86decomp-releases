---
title: x86decomp hybrid-generate
description: Command reference for `x86decomp hybrid-generate`.
---


# `x86decomp hybrid-generate`

## Usage

```text
usage: x86decomp hybrid-generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 project output
```

## Arguments

| Argument | Details |
| --- | --- |
| `project` | required · type: `path`. |
| `output` | required · type: `path`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--asm-format` | choices: `bytes`, `annotated`, `mnemonic` · default: `'bytes'`. |
| `--image-base` | type: `int` · default: `0`. |
| `--assembler-command-json` | — |
| `--symbol-map` | — |
| `--overwrite` | nargs: `0` · default: `False`. |



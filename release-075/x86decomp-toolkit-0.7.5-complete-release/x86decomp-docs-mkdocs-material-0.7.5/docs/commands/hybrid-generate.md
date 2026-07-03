---
title: x86decomp hybrid-generate
description: Exact parser-derived reference for x86decomp hybrid-generate in 0.7.5.
---

# `x86decomp hybrid-generate`

## `x86decomp hybrid-generate`

usage: x86decomp hybrid-generate [-h] [--architecture {x86,x86_64}]

### Usage

```text
x86decomp hybrid-generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 project output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |
| `--asm-format` | default: `'bytes'` · choices: `bytes`, `annotated`, `mnemonic`. No help text is declared; parser destination is `asm_format`. |
| `--image-base` | default: `0` · type: `_int`. No help text is declared; parser destination is `image_base`. |
| `--assembler-command-json` | declared. No help text is declared; parser destination is `assembler_command_json`. |
| `--symbol-map` | declared. No help text is declared; parser destination is `symbol_map`. |
| `--overwrite` | default: `False` · nargs: `0`. No help text is declared; parser destination is `overwrite`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

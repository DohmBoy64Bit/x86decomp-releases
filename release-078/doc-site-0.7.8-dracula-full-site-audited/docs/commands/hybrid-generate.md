---
title: x86decomp hybrid-generate
description: Exact v0.7.8 parser-derived reference for `x86decomp hybrid-generate`.
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

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `output` | required · type: `_path` · parser destination: `output`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--asm-format` | choices: `bytes`, `annotated`, `mnemonic` · default: `'bytes'` · parser destination: `asm_format`. No help text declared. |
| `--image-base` | type: `_int` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--assembler-command-json` | parser destination: `assembler_command_json`. No help text declared. |
| `--symbol-map` | parser destination: `symbol_map`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

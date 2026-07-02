---
title: x86decomp hybrid-generate
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/hybrid-generate.html
---

<a id="command-hybrid-generate"></a>

Section: Command reference

# `x86decomp hybrid-generate`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp hybrid-generate --help
```

Metadata: current · core

## `x86decomp hybrid-generate`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp hybrid-generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 project output
```

### Syntax example

```
x86decomp hybrid-generate ./work ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |
| `--asm-format` default: 'bytes' · choices: bytes, annotated, mnemonic | No argument help text is declared; parser destination is `asm_format`. |
| `--image-base` default: 0 · type: _int | No argument help text is declared; parser destination is `image_base`. |
| `--assembler-command-json` | No argument help text is declared; parser destination is `assembler_command_json`. |
| `--symbol-map` | No argument help text is declared; parser destination is `symbol_map`. |
| `--overwrite` nargs: 0 · default: False | No argument help text is declared; parser destination is `overwrite`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

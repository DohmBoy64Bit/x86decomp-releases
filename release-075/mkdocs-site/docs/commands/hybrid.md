---
title: x86decomp hybrid
description: Exact parser-derived reference for x86decomp hybrid in 0.7.5.
---

# `x86decomp hybrid`

Canonical capability group with 3 routes. Shared group options are shown in every exact usage string.

## `x86decomp hybrid compose`

usage: x86decomp hybrid compose [-h] run_id output

### Usage

```text
x86decomp hybrid compose [-h] run_id output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required. No help text is declared; parser destination is `run_id`. |
| `output` | required. No help text is declared; parser destination is `output`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp hybrid generate`

usage: x86decomp hybrid generate [-h] [--architecture {x86,x86_64}]

### Usage

```text
x86decomp hybrid generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 source_project output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source_project` | required. No help text is declared; parser destination is `source_project`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |
| `--asm-format` | default: `'bytes'` · choices: `bytes`, `annotated`, `mnemonic`. No help text is declared; parser destination is `asm_format`. |
| `--image-base` | default: `0` · type: `_int`. No help text is declared; parser destination is `image_base`. |
| `--assembler-command-json` | declared. No help text is declared; parser destination is `assembler_command_json`. |
| `--symbol-map` | declared. No help text is declared; parser destination is `symbol_map`. |
| `--overwrite` | default: `False` · nargs: `0`. No help text is declared; parser destination is `overwrite`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp hybrid verify`

usage: x86decomp hybrid verify [-h] composition_id

### Usage

```text
x86decomp hybrid verify [-h] composition_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `composition_id` | required. No help text is declared; parser destination is `composition_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |

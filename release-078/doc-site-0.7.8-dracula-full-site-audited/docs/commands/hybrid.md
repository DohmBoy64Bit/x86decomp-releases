---
title: x86decomp hybrid
description: Command reference for `x86decomp hybrid`.
---


# `x86decomp hybrid`

Canonical hybrid commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp hybrid [-h] [--project PROJECT] [--actor ACTOR]
                        {compose,generate,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compose` | `usage: x86decomp hybrid compose [-h] run_id output` | `native` |
| `generate` | `usage: x86decomp hybrid generate [-h] [--architecture {x86,x86_64}] [--asm-format {bytes,annotated,mnemonic}] [--image-base IMAGE_BASE] [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--symbol-map SYMBOL_MAP] [--overwrite] source_project output` | `assembly` |
| `verify` | `usage: x86decomp hybrid verify [-h] composition_id` | `native` |

### `x86decomp hybrid compose`

```text
usage: x86decomp hybrid compose [-h] run_id output
```

| Argument | Details |
| --- | --- |
| `run_id` | required. |
| `output` | required. |

### `x86decomp hybrid generate`

```text
usage: x86decomp hybrid generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 source_project output
```

| Argument | Details |
| --- | --- |
| `source_project` | required. |
| `output` | required. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--asm-format` | choices: `bytes`, `annotated`, `mnemonic` · default: `'bytes'`. |
| `--image-base` | type: `int` · default: `0`. |
| `--assembler-command-json` | — |
| `--symbol-map` | — |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp hybrid verify`

```text
usage: x86decomp hybrid verify [-h] composition_id
```

| Argument | Details |
| --- | --- |
| `composition_id` | required. |



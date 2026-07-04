---
title: x86decomp asm
description: Command reference for `x86decomp asm`.
---


# `x86decomp asm`

Canonical asm commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp asm [-h] [--project PROJECT] [--actor ACTOR]
                     {annotate,batch,list,materialize,report,verify-roundtrip} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `annotate` | `usage: x86decomp asm annotate [-h] --symbol SYMBOL --rva RVA [--image-base IMAGE_BASE] [--architecture {x86,x86_64}] source output` | `assembly` |
| `batch` | `usage: x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}] [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--image-base IMAGE_BASE] manifest output` | `assembly` |
| `list` | `usage: x86decomp asm list [-h]` | `assembly` |
| `materialize` | `usage: x86decomp asm materialize [-h] [--input-kind {bytes,assembly}] --symbol SYMBOL --rva RVA [--image-base IMAGE_BASE] [--architecture {x86,x86_64}] --symbol-map SYMBOL_MAP [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--timeout TIMEOUT] [--report REPORT] input output_source output_object output_resolved` | `assembly` |
| `report` | `usage: x86decomp asm report [-h] run_id` | `assembly` |
| `verify-roundtrip` | `usage: x86decomp asm verify-roundtrip [-h] --symbol SYMBOL --rva RVA [--image-base IMAGE_BASE] [--architecture {x86,x86_64}] --symbol-map SYMBOL_MAP [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--timeout TIMEOUT] [--report REPORT] source original output_object output_resolved` | `assembly` |

### `x86decomp asm annotate`

```text
usage: x86decomp asm annotate [-h] --symbol SYMBOL --rva RVA
                              [--image-base IMAGE_BASE]
                              [--architecture {x86,x86_64}]
                              source output
```

| Argument | Details |
| --- | --- |
| `source` | required. |
| `output` | required. |
| `--symbol` | required. |
| `--rva` | required · type: `int`. |
| `--image-base` | type: `int` · default: `0`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |

### `x86decomp asm batch`

```text
usage: x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}]
                           [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                           [--image-base IMAGE_BASE]
                           manifest output
```

| Argument | Details |
| --- | --- |
| `manifest` | required. |
| `output` | required. |
| `--format` | choices: `bytes`, `annotated`, `mnemonic` · default: `'bytes'`. |
| `--assembler-command-json` | — |
| `--image-base` | type: `int`. |

### `x86decomp asm list`

```text
usage: x86decomp asm list [-h]
```

### `x86decomp asm materialize`

```text
usage: x86decomp asm materialize [-h] [--input-kind {bytes,assembly}]
                                 --symbol SYMBOL --rva RVA
                                 [--image-base IMAGE_BASE]
                                 [--architecture {x86,x86_64}]
                                 --symbol-map SYMBOL_MAP
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--timeout TIMEOUT] [--report REPORT]
                                 input output_source output_object
                                 output_resolved
```

| Argument | Details |
| --- | --- |
| `input` | required. |
| `output_source` | required. |
| `output_object` | required. |
| `output_resolved` | required. |
| `--input-kind` | choices: `bytes`, `assembly` · default: `'bytes'`. |
| `--symbol` | required. |
| `--rva` | required · type: `int`. |
| `--image-base` | type: `int` · default: `0`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--symbol-map` | required. |
| `--assembler-command-json` | — |
| `--timeout` | type: `int` · default: `60`. |
| `--report` | — |

### `x86decomp asm report`

```text
usage: x86decomp asm report [-h] run_id
```

| Argument | Details |
| --- | --- |
| `run_id` | required. |

### `x86decomp asm verify-roundtrip`

```text
usage: x86decomp asm verify-roundtrip [-h] --symbol SYMBOL --rva RVA
                                      [--image-base IMAGE_BASE]
                                      [--architecture {x86,x86_64}]
                                      --symbol-map SYMBOL_MAP
                                      [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                      [--timeout TIMEOUT] [--report REPORT]
                                      source original output_object
                                      output_resolved
```

| Argument | Details |
| --- | --- |
| `source` | required. |
| `original` | required. |
| `output_object` | required. |
| `output_resolved` | required. |
| `--symbol` | required. |
| `--rva` | required · type: `int`. |
| `--image-base` | type: `int` · default: `0`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--symbol-map` | required. |
| `--assembler-command-json` | — |
| `--timeout` | type: `int` · default: `60`. |
| `--report` | — |



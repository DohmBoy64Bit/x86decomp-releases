---
title: x86decomp asm
description: Exact parser-derived reference for x86decomp asm in 0.7.5.
---

# `x86decomp asm`

Canonical capability group with 6 routes. Shared group options are shown in every exact usage string.

## `x86decomp asm annotate`

usage: x86decomp asm annotate [-h] --symbol SYMBOL --rva RVA

### Usage

```text
x86decomp asm annotate [-h] --symbol SYMBOL --rva RVA
                              [--image-base IMAGE_BASE]
                              [--architecture {x86,x86_64}]
                              source output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source` | required. No help text is declared; parser destination is `source`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--symbol` | required. No help text is declared; parser destination is `symbol`. |
| `--rva` | required · type: `_int`. No help text is declared; parser destination is `rva`. |
| `--image-base` | default: `0` · type: `_int`. No help text is declared; parser destination is `image_base`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp asm batch`

usage: x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}]

### Usage

```text
x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}]
                           [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                           [--image-base IMAGE_BASE]
                           manifest output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required. No help text is declared; parser destination is `manifest`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--format` | default: `'bytes'` · choices: `bytes`, `annotated`, `mnemonic`. No help text is declared; parser destination is `asm_format`. |
| `--assembler-command-json` | declared. No help text is declared; parser destination is `assembler_command_json`. |
| `--image-base` | type: `_int`. No help text is declared; parser destination is `image_base`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp asm list`

usage: x86decomp asm list [-h]

### Usage

```text
x86decomp asm list [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp asm materialize`

usage: x86decomp asm materialize [-h] [--input-kind {bytes,assembly}]

### Usage

```text
x86decomp asm materialize [-h] [--input-kind {bytes,assembly}]
                                 --symbol SYMBOL --rva RVA
                                 [--image-base IMAGE_BASE]
                                 [--architecture {x86,x86_64}]
                                 --symbol-map SYMBOL_MAP
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--timeout TIMEOUT] [--report REPORT]
                                 input output_source output_object
                                 output_resolved
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `input` | required. No help text is declared; parser destination is `input`. |
| `output_source` | required. No help text is declared; parser destination is `output_source`. |
| `output_object` | required. No help text is declared; parser destination is `output_object`. |
| `output_resolved` | required. No help text is declared; parser destination is `output_resolved`. |
| `--input-kind` | default: `'bytes'` · choices: `bytes`, `assembly`. No help text is declared; parser destination is `input_kind`. |
| `--symbol` | required. No help text is declared; parser destination is `symbol`. |
| `--rva` | required · type: `_int`. No help text is declared; parser destination is `rva`. |
| `--image-base` | default: `0` · type: `_int`. No help text is declared; parser destination is `image_base`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |
| `--symbol-map` | required. No help text is declared; parser destination is `symbol_map`. |
| `--assembler-command-json` | declared. No help text is declared; parser destination is `assembler_command_json`. |
| `--timeout` | default: `60` · type: `int`. No help text is declared; parser destination is `timeout`. |
| `--report` | declared. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp asm report`

usage: x86decomp asm report [-h] run_id

### Usage

```text
x86decomp asm report [-h] run_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required. No help text is declared; parser destination is `run_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |
## `x86decomp asm verify-roundtrip`

usage: x86decomp asm verify-roundtrip [-h] --symbol SYMBOL --rva RVA

### Usage

```text
x86decomp asm verify-roundtrip [-h] --symbol SYMBOL --rva RVA
                                      [--image-base IMAGE_BASE]
                                      [--architecture {x86,x86_64}]
                                      --symbol-map SYMBOL_MAP
                                      [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                      [--timeout TIMEOUT] [--report REPORT]
                                      source original output_object
                                      output_resolved
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source` | required. No help text is declared; parser destination is `source`. |
| `original` | required. No help text is declared; parser destination is `original`. |
| `output_object` | required. No help text is declared; parser destination is `output_object`. |
| `output_resolved` | required. No help text is declared; parser destination is `output_resolved`. |
| `--symbol` | required. No help text is declared; parser destination is `symbol`. |
| `--rva` | required · type: `_int`. No help text is declared; parser destination is `rva`. |
| `--image-base` | default: `0` · type: `_int`. No help text is declared; parser destination is `image_base`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |
| `--symbol-map` | required. No help text is declared; parser destination is `symbol_map`. |
| `--assembler-command-json` | declared. No help text is declared; parser destination is `assembler_command_json`. |
| `--timeout` | default: `60` · type: `int`. No help text is declared; parser destination is `timeout`. |
| `--report` | declared. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `assembly` | `src/x86decomp/assembly/cli.py` · `3d344a3b57ba8b3bdb778470ee7d14ce261e67b1cf69d0c07dad2548151f3d1f` |

---
title: x86decomp asm
description: Exact v0.7.8 parser-derived reference for `x86decomp asm`.
---


# `x86decomp asm`

Canonical asm commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp asm [-h] [--project PROJECT] [--actor ACTOR]
                     {annotate,batch,list,materialize,report,verify-roundtrip} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `source` | required · parser destination: `source`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--symbol` | required · parser destination: `symbol`. No help text declared. |
| `--rva` | required · type: `_int` · parser destination: `rva`. No help text declared. |
| `--image-base` | type: `_int` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |

### `x86decomp asm batch`

```text
usage: x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}]
                           [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                           [--image-base IMAGE_BASE]
                           manifest output
```

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required · parser destination: `manifest`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--format` | choices: `bytes`, `annotated`, `mnemonic` · default: `'bytes'` · parser destination: `asm_format`. No help text declared. |
| `--assembler-command-json` | parser destination: `assembler_command_json`. No help text declared. |
| `--image-base` | type: `_int` · parser destination: `image_base`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `input` | required · parser destination: `input`. No help text declared. |
| `output_source` | required · parser destination: `output_source`. No help text declared. |
| `output_object` | required · parser destination: `output_object`. No help text declared. |
| `output_resolved` | required · parser destination: `output_resolved`. No help text declared. |
| `--input-kind` | choices: `bytes`, `assembly` · default: `'bytes'` · parser destination: `input_kind`. No help text declared. |
| `--symbol` | required · parser destination: `symbol`. No help text declared. |
| `--rva` | required · type: `_int` · parser destination: `rva`. No help text declared. |
| `--image-base` | type: `_int` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--symbol-map` | required · parser destination: `symbol_map`. No help text declared. |
| `--assembler-command-json` | parser destination: `assembler_command_json`. No help text declared. |
| `--timeout` | type: `int` · default: `60` · parser destination: `timeout`. No help text declared. |
| `--report` | parser destination: `report`. No help text declared. |

### `x86decomp asm report`

```text
usage: x86decomp asm report [-h] run_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required · parser destination: `run_id`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `source` | required · parser destination: `source`. No help text declared. |
| `original` | required · parser destination: `original`. No help text declared. |
| `output_object` | required · parser destination: `output_object`. No help text declared. |
| `output_resolved` | required · parser destination: `output_resolved`. No help text declared. |
| `--symbol` | required · parser destination: `symbol`. No help text declared. |
| `--rva` | required · type: `_int` · parser destination: `rva`. No help text declared. |
| `--image-base` | type: `_int` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--symbol-map` | required · parser destination: `symbol_map`. No help text declared. |
| `--assembler-command-json` | parser destination: `assembler_command_json`. No help text declared. |
| `--timeout` | type: `int` · default: `60` · parser destination: `timeout`. No help text declared. |
| `--report` | parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| assembly cli | `src/x86decomp/assembly/cli.py` | `6c8a227f8c1a9c48a83e1f048f6160f8740e97552fa6967dea122f42fab45f88` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

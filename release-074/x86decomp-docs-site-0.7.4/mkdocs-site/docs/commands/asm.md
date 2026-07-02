---
title: x86decomp asm
description: Canonical asm commands implemented by the current capability subsystem.
original_path: commands/asm.html
---

<a id="command-asm-annotate"></a>
<a id="command-asm-batch"></a>
<a id="command-asm-list"></a>
<a id="command-asm-materialize"></a>
<a id="command-asm-report"></a>
<a id="command-asm-verify-roundtrip"></a>

Section: Command reference

# `x86decomp asm`

Canonical asm commands implemented by the current capability subsystem.

Metadata: current · canonical group · 6 runnable paths

## Help

```
x86decomp asm --help
```

Metadata: current · assembly

## `x86decomp asm annotate`

annotate command

### Usage

```
x86decomp asm annotate [-h] --symbol SYMBOL --rva RVA
                              [--image-base IMAGE_BASE]
                              [--architecture {x86,x86_64}]
                              source output
```

### Syntax example

```
x86decomp asm annotate ./candidate.c ./output.json --symbol example --rva 0x1000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source` required | No argument help text is declared; parser destination is `source`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--symbol` required | No argument help text is declared; parser destination is `symbol`. |
| `--rva` required · type: _int | No argument help text is declared; parser destination is `rva`. |
| `--image-base` default: 0 · type: _int | No argument help text is declared; parser destination is `image_base`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp asm batch`

batch command

### Usage

```
x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}]
                           [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                           [--image-base IMAGE_BASE]
                           manifest output
```

### Syntax example

```
x86decomp asm batch ./output.json ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `manifest` required | No argument help text is declared; parser destination is `manifest`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--format` default: 'bytes' · choices: bytes, annotated, mnemonic | No argument help text is declared; parser destination is `asm_format`. |
| `--assembler-command-json` | No argument help text is declared; parser destination is `assembler_command_json`. |
| `--image-base` type: _int | No argument help text is declared; parser destination is `image_base`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp asm list`

list command

### Usage

```
x86decomp asm list [-h]
```

### Syntax example

```
x86decomp asm list
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp asm materialize`

materialize command

### Usage

```
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

### Syntax example

```
x86decomp asm materialize ./input.json ./generated.asm ./generated.obj ./resolved.bin --symbol example --rva 0x1000 --symbol-map ./target.map
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `input` required | No argument help text is declared; parser destination is `input`. |
| `output_source` required | No argument help text is declared; parser destination is `output_source`. |
| `output_object` required | No argument help text is declared; parser destination is `output_object`. |
| `output_resolved` required | No argument help text is declared; parser destination is `output_resolved`. |
| `--input-kind` default: 'bytes' · choices: bytes, assembly | No argument help text is declared; parser destination is `input_kind`. |
| `--symbol` required | No argument help text is declared; parser destination is `symbol`. |
| `--rva` required · type: _int | No argument help text is declared; parser destination is `rva`. |
| `--image-base` default: 0 · type: _int | No argument help text is declared; parser destination is `image_base`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |
| `--symbol-map` required | No argument help text is declared; parser destination is `symbol_map`. |
| `--assembler-command-json` | No argument help text is declared; parser destination is `assembler_command_json`. |
| `--timeout` default: 60 · type: int | No argument help text is declared; parser destination is `timeout`. |
| `--report` | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp asm report`

report command

### Usage

```
x86decomp asm report [-h] run_id
```

### Syntax example

```
x86decomp asm report example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `run_id` required | No argument help text is declared; parser destination is `run_id`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp asm verify-roundtrip`

verify-roundtrip command

### Usage

```
x86decomp asm verify-roundtrip [-h] --symbol SYMBOL --rva RVA
                                      [--image-base IMAGE_BASE]
                                      [--architecture {x86,x86_64}]
                                      --symbol-map SYMBOL_MAP
                                      [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                      [--timeout TIMEOUT] [--report REPORT]
                                      source original output_object
                                      output_resolved
```

### Syntax example

```
x86decomp asm verify-roundtrip ./candidate.c ./original.bin ./generated.obj ./resolved.bin --symbol example --rva 0x1000 --symbol-map ./target.map
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source` required | No argument help text is declared; parser destination is `source`. |
| `original` required | No argument help text is declared; parser destination is `original`. |
| `output_object` required | No argument help text is declared; parser destination is `output_object`. |
| `output_resolved` required | No argument help text is declared; parser destination is `output_resolved`. |
| `--symbol` required | No argument help text is declared; parser destination is `symbol`. |
| `--rva` required · type: _int | No argument help text is declared; parser destination is `rva`. |
| `--image-base` default: 0 · type: _int | No argument help text is declared; parser destination is `image_base`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |
| `--symbol-map` required | No argument help text is declared; parser destination is `symbol_map`. |
| `--assembler-command-json` | No argument help text is declared; parser destination is `assembler_command_json`. |
| `--timeout` default: 60 · type: int | No argument help text is declared; parser destination is `timeout`. |
| `--report` | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

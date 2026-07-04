---
title: x86decomp asm
---

# `x86decomp asm`

Canonical asm commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp asm [-h] [--project PROJECT] [--actor ACTOR]
                     {annotate,batch,list,materialize,report,verify-roundtrip} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `annotate` | `usage: x86decomp asm annotate [-h] --symbol SYMBOL --rva RVA [--image-base IMAGE_BASE] [--architecture {x86,x86_64}] source output` |
| `batch` | `usage: x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}] [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--image-base IMAGE_BASE] manifest output` |
| `list` | `usage: x86decomp asm list [-h]` |
| `materialize` | `usage: x86decomp asm materialize [-h] [--input-kind {bytes,assembly}] --symbol SYMBOL --rva RVA [--image-base IMAGE_BASE] [--architecture {x86,x86_64}] --symbol-map SYMBOL_MAP [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--timeout TIMEOUT] [--report REPORT] input output_source output_object output_resolved` |
| `report` | `usage: x86decomp asm report [-h] run_id` |
| `verify-roundtrip` | `usage: x86decomp asm verify-roundtrip [-h] --symbol SYMBOL --rva RVA [--image-base IMAGE_BASE] [--architecture {x86,x86_64}] --symbol-map SYMBOL_MAP [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--timeout TIMEOUT] [--report REPORT] source original output_object output_resolved` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp asm annotate` | `assembly` |
| `x86decomp asm batch` | `assembly` |
| `x86decomp asm list` | `assembly` |
| `x86decomp asm materialize` | `assembly` |
| `x86decomp asm report` | `assembly` |
| `x86decomp asm verify-roundtrip` | `assembly` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.

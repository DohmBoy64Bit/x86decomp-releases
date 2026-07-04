---
title: x86decomp hybrid
---

# `x86decomp hybrid`

Canonical hybrid commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp hybrid [-h] [--project PROJECT] [--actor ACTOR]
                        {compose,generate,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `compose` | `usage: x86decomp hybrid compose [-h] run_id output` |
| `generate` | `usage: x86decomp hybrid generate [-h] [--architecture {x86,x86_64}] [--asm-format {bytes,annotated,mnemonic}] [--image-base IMAGE_BASE] [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--symbol-map SYMBOL_MAP] [--overwrite] source_project output` |
| `verify` | `usage: x86decomp hybrid verify [-h] composition_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp hybrid compose` | `native` |
| `x86decomp hybrid generate` | `assembly` |
| `x86decomp hybrid verify` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.

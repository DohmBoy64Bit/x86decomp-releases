---
title: x86decomp coff-synthesize
description: Command reference for `x86decomp coff-synthesize`.
---


# `x86decomp coff-synthesize`

## Usage

```text
usage: x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}]
                                 [--relocations RELOCATIONS]
                                 code symbol output
```

## Arguments

| Argument | Details |
| --- | --- |
| `code` | required · type: `path`. |
| `symbol` | required. |
| `output` | required · type: `path`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--relocations` | type: `path`. |



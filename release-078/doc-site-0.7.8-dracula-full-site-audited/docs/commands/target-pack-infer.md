---
title: x86decomp target-pack-infer
description: Command reference for `x86decomp target-pack-infer`.
---


# `x86decomp target-pack-infer`

## Usage

```text
usage: x86decomp target-pack-infer [-h] [--name NAME] [--pdb PDB] [--map MAP]
                                   [--object OBJECT] [--library LIBRARY]
                                   [--rebuilt-image REBUILT_IMAGE]
                                   [--decisions DECISIONS]
                                   [--reference-artifacts]
                                   primary_image output_directory
```

## Arguments

| Argument | Details |
| --- | --- |
| `primary_image` | required · type: `path`. |
| `output_directory` | required · type: `path`. |
| `--name` | — |
| `--pdb` | type: `path`. |
| `--map` | type: `path`. |
| `--object` | type: `path` · default: `[]`. |
| `--library` | type: `path` · default: `[]`. |
| `--rebuilt-image` | type: `path`. |
| `--decisions` | type: `path`. |
| `--reference-artifacts` | nargs: `0` · default: `False`. |



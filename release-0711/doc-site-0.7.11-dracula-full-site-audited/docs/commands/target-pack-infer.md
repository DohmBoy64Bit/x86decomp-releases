---
title: x86decomp target-pack-infer
description: Parser-derived command reference page for `target-pack-infer`.
---

# `x86decomp target-pack-infer`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp target-pack-infer [-h] [--name NAME] [--pdb PDB] [--map MAP]
                                   [--object OBJECT] [--library LIBRARY]
                                   [--rebuilt-image REBUILT_IMAGE]
                                   [--decisions DECISIONS]
                                   [--reference-artifacts]
                                   primary_image output_directory

positional arguments:
  primary_image
  output_directory

options:
  -h, --help            show this help message and exit
  --name NAME
  --pdb PDB
  --map MAP
  --object OBJECT
  --library LIBRARY
  --rebuilt-image REBUILT_IMAGE
  --decisions DECISIONS
  --reference-artifacts
```

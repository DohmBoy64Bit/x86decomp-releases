---
title: x86decomp target-pack-infer
description: Exact v0.7.8 parser-derived reference for `x86decomp target-pack-infer`.
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

| Argument | Exact parser declaration |
| --- | --- |
| `primary_image` | required · type: `_path` · parser destination: `primary_image`. No help text declared. |
| `output_directory` | required · type: `_path` · parser destination: `output_directory`. No help text declared. |
| `--name` | parser destination: `name`. No help text declared. |
| `--pdb` | type: `_path` · parser destination: `pdb`. No help text declared. |
| `--map` | type: `_path` · parser destination: `map`. No help text declared. |
| `--object` | type: `_path` · default: `[]` · parser destination: `object`. No help text declared. |
| `--library` | type: `_path` · default: `[]` · parser destination: `library`. No help text declared. |
| `--rebuilt-image` | type: `_path` · parser destination: `rebuilt_image`. No help text declared. |
| `--decisions` | type: `_path` · parser destination: `decisions`. No help text declared. |
| `--reference-artifacts` | nargs: `0` · default: `False` · parser destination: `reference_artifacts`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

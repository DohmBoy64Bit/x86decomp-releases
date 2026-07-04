---
title: x86decomp target-pack-infer
description: Exact parser-derived reference for x86decomp target-pack-infer in 0.7.5.
---

# `x86decomp target-pack-infer`

## `x86decomp target-pack-infer`

usage: x86decomp target-pack-infer [-h] [--name NAME] [--pdb PDB] [--map MAP]

### Usage

```text
x86decomp target-pack-infer [-h] [--name NAME] [--pdb PDB] [--map MAP]
                                   [--object OBJECT] [--library LIBRARY]
                                   [--rebuilt-image REBUILT_IMAGE]
                                   [--decisions DECISIONS]
                                   [--reference-artifacts]
                                   primary_image output_directory
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `primary_image` | required · type: `_path`. No help text is declared; parser destination is `primary_image`. |
| `output_directory` | required · type: `_path`. No help text is declared; parser destination is `output_directory`. |
| `--name` | declared. No help text is declared; parser destination is `name`. |
| `--pdb` | type: `_path`. No help text is declared; parser destination is `pdb`. |
| `--map` | type: `_path`. No help text is declared; parser destination is `map`. |
| `--object` | default: `[]` · type: `_path`. No help text is declared; parser destination is `object`. |
| `--library` | default: `[]` · type: `_path`. No help text is declared; parser destination is `library`. |
| `--rebuilt-image` | type: `_path`. No help text is declared; parser destination is `rebuilt_image`. |
| `--decisions` | type: `_path`. No help text is declared; parser destination is `decisions`. |
| `--reference-artifacts` | default: `False` · nargs: `0`. No help text is declared; parser destination is `reference_artifacts`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

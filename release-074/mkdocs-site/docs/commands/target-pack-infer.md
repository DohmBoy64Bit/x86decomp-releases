---
title: x86decomp target-pack-infer
description: infer a fact-preserving target pack and template plan
original_path: commands/target-pack-infer.html
---

<a id="command-target-pack-infer"></a>

Section: Command reference

# `x86decomp target-pack-infer`

infer a fact-preserving target pack and template plan

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp target-pack-infer --help
```

Metadata: current · core

## `x86decomp target-pack-infer`

infer a fact-preserving target pack and template plan

### Usage

```
x86decomp target-pack-infer [-h] [--name NAME] [--pdb PDB] [--map MAP]
                                   [--object OBJECT] [--library LIBRARY]
                                   [--rebuilt-image REBUILT_IMAGE]
                                   [--decisions DECISIONS]
                                   [--reference-artifacts]
                                   primary_image output_directory
```

### Syntax example

```
x86decomp target-pack-infer ./target.exe ./output
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `primary_image` required · type: _path | No argument help text is declared; parser destination is `primary_image`. |
| `output_directory` required · type: _path | No argument help text is declared; parser destination is `output_directory`. |
| `--name` | No argument help text is declared; parser destination is `name`. |
| `--pdb` type: _path | No argument help text is declared; parser destination is `pdb`. |
| `--map` type: _path | No argument help text is declared; parser destination is `map`. |
| `--object` default: [] · type: _path | No argument help text is declared; parser destination is `object`. |
| `--library` default: [] · type: _path | No argument help text is declared; parser destination is `library`. |
| `--rebuilt-image` type: _path | No argument help text is declared; parser destination is `rebuilt_image`. |
| `--decisions` type: _path | No argument help text is declared; parser destination is `decisions`. |
| `--reference-artifacts` nargs: 0 · default: False | No argument help text is declared; parser destination is `reference_artifacts`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

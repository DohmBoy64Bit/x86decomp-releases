---
title: x86decomp corpus-generate
description: generate a deterministic parameterized C/C++ source corpus
original_path: commands/corpus-generate.html
---

<a id="command-corpus-generate"></a>

Section: Command reference

# `x86decomp corpus-generate`

generate a deterministic parameterized C/C++ source corpus

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp corpus-generate --help
```

Metadata: current · core

## `x86decomp corpus-generate`

generate a deterministic parameterized C/C++ source corpus

### Usage

```
x86decomp corpus-generate [-h] [--cases-per-family CASES_PER_FAMILY]
                                 [--seed SEED] [--c-only] [--cpp-only]
                                 [--report REPORT]
                                 output_directory
```

### Syntax example

```
x86decomp corpus-generate ./output
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output_directory` required · type: _path | No argument help text is declared; parser destination is `output_directory`. |
| `--cases-per-family` default: 8 · type: int | No argument help text is declared; parser destination is `cases_per_family`. |
| `--seed` default: 2262745310 · type: _int | No argument help text is declared; parser destination is `seed`. |
| `--c-only` nargs: 0 · default: False | No argument help text is declared; parser destination is `c_only`. |
| `--cpp-only` nargs: 0 · default: False | No argument help text is declared; parser destination is `cpp_only`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

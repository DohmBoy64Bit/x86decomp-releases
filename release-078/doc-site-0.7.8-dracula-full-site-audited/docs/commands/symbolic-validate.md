---
title: x86decomp symbolic-validate
description: Exact v0.7.8 parser-derived reference for `x86decomp symbolic-validate`.
---


# `x86decomp symbolic-validate`

## Usage

```text
usage: x86decomp symbolic-validate [-h] [--architecture {x86,x86_64}]
                                   [--input-register INPUT_REGISTER]
                                   [--stack-argument-words STACK_ARGUMENT_WORDS]
                                   [--output-register OUTPUT_REGISTER]
                                   [--max-steps MAX_STEPS]
                                   [--max-paths MAX_PATHS] [--report REPORT]
                                   target candidate
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target` | required · type: `_path` · parser destination: `target`. No help text declared. |
| `candidate` | required · type: `_path` · parser destination: `candidate`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--input-register` | default: `[]` · parser destination: `input_register`. No help text declared. |
| `--stack-argument-words` | type: `int` · default: `0` · parser destination: `stack_argument_words`. No help text declared. |
| `--output-register` | parser destination: `output_register`. No help text declared. |
| `--max-steps` | type: `int` · default: `1000` · parser destination: `max_steps`. No help text declared. |
| `--max-paths` | type: `int` · default: `64` · parser destination: `max_paths`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

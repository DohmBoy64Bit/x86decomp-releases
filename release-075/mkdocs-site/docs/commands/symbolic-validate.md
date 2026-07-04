---
title: x86decomp symbolic-validate
description: Exact parser-derived reference for x86decomp symbolic-validate in 0.7.5.
---

# `x86decomp symbolic-validate`

## `x86decomp symbolic-validate`

usage: x86decomp symbolic-validate [-h] [--architecture {x86,x86_64}]

### Usage

```text
x86decomp symbolic-validate [-h] [--architecture {x86,x86_64}]
                                   [--input-register INPUT_REGISTER]
                                   [--stack-argument-words STACK_ARGUMENT_WORDS]
                                   [--output-register OUTPUT_REGISTER]
                                   [--max-steps MAX_STEPS]
                                   [--max-paths MAX_PATHS] [--report REPORT]
                                   target candidate
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target` | required · type: `_path`. No help text is declared; parser destination is `target`. |
| `candidate` | required · type: `_path`. No help text is declared; parser destination is `candidate`. |
| `--architecture` | default: `'x86'` · choices: `x86`, `x86_64`. No help text is declared; parser destination is `architecture`. |
| `--input-register` | default: `[]`. No help text is declared; parser destination is `input_register`. |
| `--stack-argument-words` | default: `0` · type: `int`. No help text is declared; parser destination is `stack_argument_words`. |
| `--output-register` | declared. No help text is declared; parser destination is `output_register`. |
| `--max-steps` | default: `1000` · type: `int`. No help text is declared; parser destination is `max_steps`. |
| `--max-paths` | default: `64` · type: `int`. No help text is declared; parser destination is `max_paths`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

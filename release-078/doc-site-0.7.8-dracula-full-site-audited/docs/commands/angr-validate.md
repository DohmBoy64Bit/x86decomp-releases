---
title: x86decomp angr-validate
description: Command reference for `x86decomp angr-validate`.
---


# `x86decomp angr-validate`

## Usage

```text
usage: x86decomp angr-validate [-h] [--architecture {x86,x86_64}]
                               [--input-register INPUT_REGISTER]
                               [--stack-argument-words STACK_ARGUMENT_WORDS]
                               [--output-register OUTPUT_REGISTER]
                               [--max-steps MAX_STEPS] [--max-paths MAX_PATHS]
                               [--report REPORT]
                               target candidate
```

## Arguments

| Argument | Details |
| --- | --- |
| `target` | required · type: `path`. |
| `candidate` | required · type: `path`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--input-register` | default: `[]`. |
| `--stack-argument-words` | type: `int` · default: `0`. |
| `--output-register` | — |
| `--max-steps` | type: `int` · default: `1000`. |
| `--max-paths` | type: `int` · default: `64`. |
| `--report` | type: `path`. |



---
title: x86decomp crosscheck-ghidra
description: Command reference for `x86decomp crosscheck-ghidra`.
---


# `x86decomp crosscheck-ghidra`

## Usage

```text
usage: x86decomp crosscheck-ghidra [-h] --base BASE
                                   [--architecture {x86,x86_64}]
                                   [--report REPORT]
                                   instructions_jsonl code
```

## Arguments

| Argument | Details |
| --- | --- |
| `instructions_jsonl` | required · type: `path`. |
| `code` | required · type: `path`. |
| `--base` | required · type: `int`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--report` | type: `path`. |



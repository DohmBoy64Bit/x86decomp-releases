---
title: x86decomp work-create
description: Command reference for `x86decomp work-create`.
---


# `x86decomp work-create`

## Usage

```text
usage: x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY]
                             database function_id {matching,functional} kind
                             instructions
```

## Arguments

| Argument | Details |
| --- | --- |
| `database` | required · type: `path`. |
| `function_id` | required. |
| `mode` | required · choices: `matching`, `functional`. |
| `kind` | required. |
| `instructions` | required. |
| `--validator` | required. |
| `--priority` | type: `int` · default: `0`. |



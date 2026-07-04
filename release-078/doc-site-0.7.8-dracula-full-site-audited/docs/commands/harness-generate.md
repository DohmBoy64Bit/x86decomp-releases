---
title: x86decomp harness-generate
description: Command reference for `x86decomp harness-generate`.
---


# `x86decomp harness-generate`

## Usage

```text
usage: x86decomp harness-generate [-h]
                                  [--pointer-parameters POINTER_PARAMETERS]
                                  [--no-observe-pointers]
                                  [--max-instructions MAX_INSTRUCTIONS]
                                  [--timeout-ms TIMEOUT_MS]
                                  abi_contract output
```

## Arguments

| Argument | Details |
| --- | --- |
| `abi_contract` | required · type: `path`. |
| `output` | required · type: `path`. |
| `--pointer-parameters` | type: `path`. |
| `--no-observe-pointers` | nargs: `0` · default: `False`. |
| `--max-instructions` | type: `int` · default: `100000`. |
| `--timeout-ms` | type: `int` · default: `1000`. |



---
title: x86decomp patch-image
description: Command reference for `x86decomp patch-image`.
---


# `x86decomp patch-image`

## Usage

```text
usage: x86decomp patch-image [-h] --rva RVA
                             [--expected-original-sha256 EXPECTED_ORIGINAL_SHA256]
                             [--expected-function-sha256 EXPECTED_FUNCTION_SHA256]
                             [--report REPORT]
                             original candidate output
```

## Arguments

| Argument | Details |
| --- | --- |
| `original` | required · type: `path`. |
| `candidate` | required · type: `path`. |
| `output` | required · type: `path`. |
| `--rva` | required · type: `int`. |
| `--expected-original-sha256` | — |
| `--expected-function-sha256` | — |
| `--report` | type: `path`. |



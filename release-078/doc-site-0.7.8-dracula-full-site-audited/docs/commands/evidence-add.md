---
title: x86decomp evidence-add
description: Command reference for `x86decomp evidence-add`.
---


# `x86decomp evidence-add`

## Usage

```text
usage: x86decomp evidence-add [-h]
                              --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
                              --source SOURCE --locator LOCATOR
                              --assertion ASSERTION
                              --independent-group INDEPENDENT_GROUP
                              [--file FILE] [--id ID]
                              project
```

## Arguments

| Argument | Details |
| --- | --- |
| `project` | required · type: `path`. |
| `--kind` | required · choices: `binary_bytes`, `static_analysis`, `dynamic_trace`, `compiler_output`, `debug_symbol`, `external_document`, `human_review`. |
| `--source` | required. |
| `--locator` | required. |
| `--assertion` | required. |
| `--independent-group` | required. |
| `--file` | type: `path`. |
| `--id` | — |



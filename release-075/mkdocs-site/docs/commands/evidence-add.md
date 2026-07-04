---
title: x86decomp evidence-add
description: Exact parser-derived reference for x86decomp evidence-add in 0.7.5.
---

# `x86decomp evidence-add`

## `x86decomp evidence-add`

usage: x86decomp evidence-add [-h]

### Usage

```text
x86decomp evidence-add [-h]
                              --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
                              --source SOURCE --locator LOCATOR
                              --assertion ASSERTION
                              --independent-group INDEPENDENT_GROUP
                              [--file FILE] [--id ID]
                              project
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--kind` | required · choices: `binary_bytes`, `static_analysis`, `dynamic_trace`, `compiler_output`, `debug_symbol`, `external_document`, `human_review`. No help text is declared; parser destination is `kind`. |
| `--source` | required. No help text is declared; parser destination is `source`. |
| `--locator` | required. No help text is declared; parser destination is `locator`. |
| `--assertion` | required. No help text is declared; parser destination is `assertion`. |
| `--independent-group` | required. No help text is declared; parser destination is `independent_group`. |
| `--file` | type: `_path`. No help text is declared; parser destination is `file`. |
| `--id` | declared. No help text is declared; parser destination is `id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

---
title: x86decomp workflow-update
description: Exact parser-derived reference for x86decomp workflow-update in 0.7.5.
---

# `x86decomp workflow-update`

## `x86decomp workflow-update`

usage: x86decomp workflow-update [-h]

### Usage

```text
x86decomp workflow-update [-h]
                                 [--source-stage {original_bytes,generated_assembly,decompiler_candidate,human_candidate,accepted_source}]
                                 [--matching-status {not_started,decompiled,compiles,abi_compatible,instruction_similar,byte_matched,image_integrated,full_relink_validated,blocked}]
                                 [--functional-status {not_started,decompiled,compiles,abi_compatible,differentially_validated,symbolically_bounded,integration_validated,blocked}]
                                 [--candidate CANDIDATE]
                                 [--compiler-profile COMPILER_PROFILE]
                                 [--report-kind REPORT_KIND]
                                 [--report-path REPORT_PATH]
                                 [--blocker BLOCKER] [--allow-regression]
                                 project function_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `function_id` | required. No help text is declared; parser destination is `function_id`. |
| `--source-stage` | choices: `original_bytes`, `generated_assembly`, `decompiler_candidate`, `human_candidate`, `accepted_source`. No help text is declared; parser destination is `source_stage`. |
| `--matching-status` | choices: `not_started`, `decompiled`, `compiles`, `abi_compatible`, `instruction_similar`, `byte_matched`, `image_integrated`, `full_relink_validated`, `blocked`. No help text is declared; parser destination is `matching_status`. |
| `--functional-status` | choices: `not_started`, `decompiled`, `compiles`, `abi_compatible`, `differentially_validated`, `symbolically_bounded`, `integration_validated`, `blocked`. No help text is declared; parser destination is `functional_status`. |
| `--candidate` | declared. No help text is declared; parser destination is `candidate`. |
| `--compiler-profile` | declared. No help text is declared; parser destination is `compiler_profile`. |
| `--report-kind` | declared. No help text is declared; parser destination is `report_kind`. |
| `--report-path` | declared. No help text is declared; parser destination is `report_path`. |
| `--blocker` | declared. No help text is declared; parser destination is `blocker`. |
| `--allow-regression` | default: `False` · nargs: `0`. No help text is declared; parser destination is `allow_regression`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

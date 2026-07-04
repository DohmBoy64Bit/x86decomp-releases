---
title: x86decomp workflow-update
description: Command reference for `x86decomp workflow-update`.
---


# `x86decomp workflow-update`

## Usage

```text
usage: x86decomp workflow-update [-h]
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

## Arguments

| Argument | Details |
| --- | --- |
| `project` | required · type: `path`. |
| `function_id` | required. |
| `--source-stage` | choices: `original_bytes`, `generated_assembly`, `decompiler_candidate`, `human_candidate`, `accepted_source`. |
| `--matching-status` | choices: `not_started`, `decompiled`, `compiles`, `abi_compatible`, `instruction_similar`, `byte_matched`, `image_integrated`, `full_relink_validated`, `blocked`. |
| `--functional-status` | choices: `not_started`, `decompiled`, `compiles`, `abi_compatible`, `differentially_validated`, `symbolically_bounded`, `integration_validated`, `blocked`. |
| `--candidate` | — |
| `--compiler-profile` | — |
| `--report-kind` | — |
| `--report-path` | — |
| `--blocker` | — |
| `--allow-regression` | nargs: `0` · default: `False`. |



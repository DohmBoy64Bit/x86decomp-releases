---
title: x86decomp workflow-update
description: Parser-derived command reference page for `workflow-update`.
---

# `x86decomp workflow-update`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

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

positional arguments:
  project
  function_id

options:
  -h, --help            show this help message and exit
  --source-stage {original_bytes,generated_assembly,decompiler_candidate,human_candidate,accepted_source}
  --matching-status {not_started,decompiled,compiles,abi_compatible,instruction_similar,byte_matched,image_integrated,full_relink_validated,blocked}
  --functional-status {not_started,decompiled,compiles,abi_compatible,differentially_validated,symbolically_bounded,integration_validated,blocked}
  --candidate CANDIDATE
  --compiler-profile COMPILER_PROFILE
  --report-kind REPORT_KIND
  --report-path REPORT_PATH
  --blocker BLOCKER
  --allow-regression
```

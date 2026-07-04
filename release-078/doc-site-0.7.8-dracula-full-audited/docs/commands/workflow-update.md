---
title: x86decomp workflow-update
---

# `x86decomp workflow-update`

usage: x86decomp workflow-update [-h]

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

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.

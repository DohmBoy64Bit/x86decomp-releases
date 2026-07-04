---
title: x86decomp workflow-update
description: Exact v0.7.8 parser-derived reference for `x86decomp workflow-update`.
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

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `function_id` | required · parser destination: `function_id`. No help text declared. |
| `--source-stage` | choices: `original_bytes`, `generated_assembly`, `decompiler_candidate`, `human_candidate`, `accepted_source` · parser destination: `source_stage`. No help text declared. |
| `--matching-status` | choices: `not_started`, `decompiled`, `compiles`, `abi_compatible`, `instruction_similar`, `byte_matched`, `image_integrated`, `full_relink_validated`, `blocked` · parser destination: `matching_status`. No help text declared. |
| `--functional-status` | choices: `not_started`, `decompiled`, `compiles`, `abi_compatible`, `differentially_validated`, `symbolically_bounded`, `integration_validated`, `blocked` · parser destination: `functional_status`. No help text declared. |
| `--candidate` | parser destination: `candidate`. No help text declared. |
| `--compiler-profile` | parser destination: `compiler_profile`. No help text declared. |
| `--report-kind` | parser destination: `report_kind`. No help text declared. |
| `--report-path` | parser destination: `report_path`. No help text declared. |
| `--blocker` | parser destination: `blocker`. No help text declared. |
| `--allow-regression` | nargs: `0` · default: `False` · parser destination: `allow_regression`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.

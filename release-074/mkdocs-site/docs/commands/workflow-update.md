---
title: x86decomp workflow-update
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/workflow-update.html
---

<a id="command-workflow-update"></a>

Section: Command reference

# `x86decomp workflow-update`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp workflow-update --help
```

Metadata: current · core

## `x86decomp workflow-update`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
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

### Syntax example

```
x86decomp workflow-update ./work pe-rva:00001000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `function_id` required | No argument help text is declared; parser destination is `function_id`. |
| `--source-stage` choices: original_bytes, generated_assembly, decompiler_candidate, human_candidate, accepted_source | No argument help text is declared; parser destination is `source_stage`. |
| `--matching-status` choices: not_started, decompiled, compiles, abi_compatible, instruction_similar, byte_matched, image_integrated, full_relink_validated, blocked | No argument help text is declared; parser destination is `matching_status`. |
| `--functional-status` choices: not_started, decompiled, compiles, abi_compatible, differentially_validated, symbolically_bounded, integration_validated, blocked | No argument help text is declared; parser destination is `functional_status`. |
| `--candidate` | No argument help text is declared; parser destination is `candidate`. |
| `--compiler-profile` | No argument help text is declared; parser destination is `compiler_profile`. |
| `--report-kind` | No argument help text is declared; parser destination is `report_kind`. |
| `--report-path` | No argument help text is declared; parser destination is `report_path`. |
| `--blocker` | No argument help text is declared; parser destination is `blocker`. |
| `--allow-regression` nargs: 0 · default: False | No argument help text is declared; parser destination is `allow_regression`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

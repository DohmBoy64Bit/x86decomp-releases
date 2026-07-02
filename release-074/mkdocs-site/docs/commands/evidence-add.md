---
title: x86decomp evidence-add
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/evidence-add.html
---

<a id="command-evidence-add"></a>

Section: Command reference

# `x86decomp evidence-add`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp evidence-add --help
```

Metadata: current · core

## `x86decomp evidence-add`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp evidence-add [-h]
                              --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
                              --source SOURCE --locator LOCATOR
                              --assertion ASSERTION
                              --independent-group INDEPENDENT_GROUP
                              [--file FILE] [--id ID]
                              project
```

### Syntax example

```
x86decomp evidence-add ./work --kind binary_bytes --source ./candidate.c --locator pe-rva:00001000 --assertion bytes-match --independent-group ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--kind` required · choices: binary_bytes, static_analysis, dynamic_trace, compiler_output, debug_symbol, external_document, human_review | No argument help text is declared; parser destination is `kind`. |
| `--source` required | No argument help text is declared; parser destination is `source`. |
| `--locator` required | No argument help text is declared; parser destination is `locator`. |
| `--assertion` required | No argument help text is declared; parser destination is `assertion`. |
| `--independent-group` required | No argument help text is declared; parser destination is `independent_group`. |
| `--file` type: _path | No argument help text is declared; parser destination is `file`. |
| `--id` | No argument help text is declared; parser destination is `id`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

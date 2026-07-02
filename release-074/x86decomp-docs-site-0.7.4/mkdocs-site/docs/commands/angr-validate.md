---
title: x86decomp angr-validate
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/angr-validate.html
---

<a id="command-angr-validate"></a>

Section: Command reference

# `x86decomp angr-validate`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp angr-validate --help
```

Metadata: current · core

## `x86decomp angr-validate`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp angr-validate [-h] [--architecture {x86,x86_64}]
                               [--input-register INPUT_REGISTER]
                               [--stack-argument-words STACK_ARGUMENT_WORDS]
                               [--output-register OUTPUT_REGISTER]
                               [--max-steps MAX_STEPS] [--max-paths MAX_PATHS]
                               [--report REPORT]
                               target candidate
```

### Syntax example

```
x86decomp angr-validate ./target.exe ./candidate.bin
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `target` required · type: _path | No argument help text is declared; parser destination is `target`. |
| `candidate` required · type: _path | No argument help text is declared; parser destination is `candidate`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |
| `--input-register` default: [] | No argument help text is declared; parser destination is `input_register`. |
| `--stack-argument-words` default: 0 · type: int | No argument help text is declared; parser destination is `stack_argument_words`. |
| `--output-register` | No argument help text is declared; parser destination is `output_register`. |
| `--max-steps` default: 1000 · type: int | No argument help text is declared; parser destination is `max_steps`. |
| `--max-paths` default: 64 · type: int | No argument help text is declared; parser destination is `max_paths`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.

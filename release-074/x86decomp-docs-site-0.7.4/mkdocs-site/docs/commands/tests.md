---
title: x86decomp tests
description: Canonical tests commands implemented by the current capability subsystem.
original_path: commands/tests.html
---

<a id="command-tests-add"></a>
<a id="command-tests-explain"></a>
<a id="command-tests-list"></a>
<a id="command-tests-promote-counterexample"></a>
<a id="command-tests-synthesize"></a>

Section: Command reference

# `x86decomp tests`

Canonical tests commands implemented by the current capability subsystem.

Metadata: current · canonical group · 5 runnable paths

## Help

```
x86decomp tests --help
```

Metadata: current · reconstruction

## `x86decomp tests add`

add command

### Usage

```
x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON
                           --evidence-json EVIDENCE_JSON
                           name scope_kind scope_id test_kind relative_path
                           content_file
```

### Syntax example

```
x86decomp tests add example function pe-rva:00001000 analysis src/candidate.c ./input.json --applicability-json ./output.json --evidence-json ./evidence.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `scope_kind` required | No argument help text is declared; parser destination is `scope_kind`. |
| `scope_id` required | No argument help text is declared; parser destination is `scope_id`. |
| `test_kind` required | No argument help text is declared; parser destination is `test_kind`. |
| `relative_path` required | No argument help text is declared; parser destination is `relative_path`. |
| `content_file` required | No argument help text is declared; parser destination is `content_file`. |
| `--applicability-json` required | No argument help text is declared; parser destination is `applicability_json`. |
| `--evidence-json` required | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp tests explain`

explain command

### Usage

```
x86decomp tests explain [-h] test_id
```

### Syntax example

```
x86decomp tests explain example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `test_id` required | No argument help text is declared; parser destination is `test_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp tests list`

list command

### Usage

```
x86decomp tests list [-h]
```

### Syntax example

```
x86decomp tests list
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp tests promote-counterexample`

promote-counterexample command

### Usage

```
x86decomp tests promote-counterexample [-h] [--name NAME]
                                              counterexample_id
```

### Syntax example

```
x86decomp tests promote-counterexample 1
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `counterexample_id` required | No argument help text is declared; parser destination is `counterexample_id`. |
| `--name` | No argument help text is declared; parser destination is `name`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp tests synthesize`

synthesize command

### Usage

```
x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id
```

### Syntax example

```
x86decomp tests synthesize function pe-rva:00001000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `scope_kind` required | No argument help text is declared; parser destination is `scope_kind`. |
| `scope_id` required | No argument help text is declared; parser destination is `scope_id`. |
| `--name` | No argument help text is declared; parser destination is `name`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

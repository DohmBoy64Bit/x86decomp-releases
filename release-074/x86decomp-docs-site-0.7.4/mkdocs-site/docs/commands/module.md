---
title: x86decomp module
description: Canonical module commands implemented by the current capability subsystem.
original_path: commands/module.html
---

<a id="command-module-add-member"></a>
<a id="command-module-add-unit-member"></a>
<a id="command-module-create"></a>
<a id="command-module-create-unit"></a>
<a id="command-module-list"></a>
<a id="command-module-show"></a>
<a id="command-module-show-unit"></a>

Section: Command reference

# `x86decomp module`

Canonical module commands implemented by the current capability subsystem.

Metadata: current · canonical group · 7 runnable paths

## Help

```
x86decomp module --help
```

Metadata: current · reconstruction

## `x86decomp module add-member`

add-member command

### Usage

```
x86decomp module add-member [-h] [--ordinal ORDINAL]
                                   [--evidence-json EVIDENCE_JSON]
                                   module_id member_kind member_id
```

### Syntax example

```
x86decomp module add-member example-001 analysis example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `module_id` required | No argument help text is declared; parser destination is `module_id`. |
| `member_kind` required | No argument help text is declared; parser destination is `member_kind`. |
| `member_id` required | No argument help text is declared; parser destination is `member_id`. |
| `--ordinal` default: 0 · type: int | No argument help text is declared; parser destination is `ordinal`. |
| `--evidence-json` | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp module add-unit-member`

add-unit-member command

### Usage

```
x86decomp module add-unit-member [-h] [--linkage LINKAGE]
                                        [--ordinal ORDINAL]
                                        unit_id member_kind member_id
```

### Syntax example

```
x86decomp module add-unit-member example-001 analysis example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `unit_id` required | No argument help text is declared; parser destination is `unit_id`. |
| `member_kind` required | No argument help text is declared; parser destination is `member_kind`. |
| `member_id` required | No argument help text is declared; parser destination is `member_id`. |
| `--linkage` default: 'external' | No argument help text is declared; parser destination is `linkage`. |
| `--ordinal` default: 0 · type: int | No argument help text is declared; parser destination is `ordinal`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp module create`

create command

### Usage

```
x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH]
                               [--confidence CONFIDENCE]
                               [--evidence-json EVIDENCE_JSON]
                               name
```

### Syntax example

```
x86decomp module create example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `--kind` default: 'static-library' | No argument help text is declared; parser destination is `kind`. |
| `--source-path` | No argument help text is declared; parser destination is `source_path`. |
| `--confidence` default: 1.0 · type: float | No argument help text is declared; parser destination is `confidence`. |
| `--evidence-json` | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp module create-unit`

create-unit command

### Usage

```
x86decomp module create-unit [-h] [--module-id MODULE_ID]
                                    [--language LANGUAGE]
                                    [--confidence CONFIDENCE]
                                    [--evidence-json EVIDENCE_JSON]
                                    source_path
```

### Syntax example

```
x86decomp module create-unit ./candidate.c
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source_path` required | No argument help text is declared; parser destination is `source_path`. |
| `--module-id` | No argument help text is declared; parser destination is `module_id`. |
| `--language` default: 'cpp' | No argument help text is declared; parser destination is `language`. |
| `--confidence` default: 1.0 · type: float | No argument help text is declared; parser destination is `confidence`. |
| `--evidence-json` | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp module list`

list command

### Usage

```
x86decomp module list [-h]
```

### Syntax example

```
x86decomp module list
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp module show`

show command

### Usage

```
x86decomp module show [-h] module_id
```

### Syntax example

```
x86decomp module show example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `module_id` required | No argument help text is declared; parser destination is `module_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp module show-unit`

show-unit command

### Usage

```
x86decomp module show-unit [-h] unit_id
```

### Syntax example

```
x86decomp module show-unit example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `unit_id` required | No argument help text is declared; parser destination is `unit_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

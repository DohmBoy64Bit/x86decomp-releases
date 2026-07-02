---
title: x86decomp abi
description: Canonical abi commands implemented by the current capability subsystem.
original_path: commands/abi.html
---

<a id="command-abi-compare"></a>
<a id="command-abi-export"></a>
<a id="command-abi-recover"></a>
<a id="command-abi-shim"></a>
<a id="command-abi-show"></a>
<a id="command-abi-verify"></a>

Section: Command reference

# `x86decomp abi`

Canonical abi commands implemented by the current capability subsystem.

Metadata: current · canonical group · 6 runnable paths

## Help

```
x86decomp abi --help
```

Metadata: current · reconstruction

## `x86decomp abi compare`

compare command

### Usage

```
x86decomp abi compare [-h] left_id right_id
```

### Syntax example

```
x86decomp abi compare example-001 example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `left_id` required | No argument help text is declared; parser destination is `left_id`. |
| `right_id` required | No argument help text is declared; parser destination is `right_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp abi export`

export command

### Usage

```
x86decomp abi export [-h] contract_id output
```

### Syntax example

```
x86decomp abi export ./contract.json ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `contract_id` required | No argument help text is declared; parser destination is `contract_id`. |
| `output` required | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp abi recover`

recover command

### Usage

```
x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON
                             subject_kind subject_id architecture
                             contract_json
```

### Syntax example

```
x86decomp abi recover analysis example-001 example ./output.json --evidence-json ./evidence.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `subject_kind` required | No argument help text is declared; parser destination is `subject_kind`. |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |
| `architecture` required | No argument help text is declared; parser destination is `architecture`. |
| `contract_json` required | No argument help text is declared; parser destination is `contract_json`. |
| `--evidence-json` required | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp abi shim`

shim command

### Usage

```
x86decomp abi shim [-h] [--kind KIND] contract_id source_path
```

### Syntax example

```
x86decomp abi shim ./contract.json ./candidate.c
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `contract_id` required | No argument help text is declared; parser destination is `contract_id`. |
| `source_path` required | No argument help text is declared; parser destination is `source_path`. |
| `--kind` default: 'wrapped' | No argument help text is declared; parser destination is `kind`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp abi show`

show command

### Usage

```
x86decomp abi show [-h] contract_id
```

### Syntax example

```
x86decomp abi show ./contract.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `contract_id` required | No argument help text is declared; parser destination is `contract_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp abi verify`

verify command

### Usage

```
x86decomp abi verify [-h] contract_id
```

### Syntax example

```
x86decomp abi verify ./contract.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `contract_id` required | No argument help text is declared; parser destination is `contract_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

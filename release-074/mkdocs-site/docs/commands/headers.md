---
title: x86decomp headers
description: Canonical headers commands implemented by the current capability subsystem.
original_path: commands/headers.html
---

<a id="command-headers-create"></a>
<a id="command-headers-cycles"></a>
<a id="command-headers-declare"></a>
<a id="command-headers-explain"></a>
<a id="command-headers-include"></a>
<a id="command-headers-synthesize"></a>
<a id="command-headers-validate"></a>

Section: Command reference

# `x86decomp headers`

Canonical headers commands implemented by the current capability subsystem.

Metadata: current · canonical group · 7 runnable paths

## Help

```
x86decomp headers --help
```

Metadata: current · reconstruction

## `x86decomp headers create`

create command

### Usage

```
x86decomp headers create [-h] [--visibility VISIBILITY] path
```

### Syntax example

```
x86decomp headers create ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |
| `--visibility` default: 'private' | No argument help text is declared; parser destination is `visibility`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp headers cycles`

cycles command

### Usage

```
x86decomp headers cycles [-h]
```

### Syntax example

```
x86decomp headers cycles
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp headers declare`

declare command

### Usage

```
x86decomp headers declare [-h] [--kind KIND] [--confidence CONFIDENCE]
                                 [--evidence-json EVIDENCE_JSON]
                                 header_id symbol_id declaration
```

### Syntax example

```
x86decomp headers declare example-001 example-001 example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `header_id` required | No argument help text is declared; parser destination is `header_id`. |
| `symbol_id` required | No argument help text is declared; parser destination is `symbol_id`. |
| `declaration` required | No argument help text is declared; parser destination is `declaration`. |
| `--kind` default: 'function' | No argument help text is declared; parser destination is `kind`. |
| `--confidence` default: 1.0 · type: float | No argument help text is declared; parser destination is `confidence`. |
| `--evidence-json` | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp headers explain`

explain command

### Usage

```
x86decomp headers explain [-h] header_id
```

### Syntax example

```
x86decomp headers explain example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `header_id` required | No argument help text is declared; parser destination is `header_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp headers include`

include command

### Usage

```
x86decomp headers include [-h] --reason REASON
                                 source_header_id target_header_id
```

### Syntax example

```
x86decomp headers include ./candidate.c ./target.exe --reason reviewed-change
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source_header_id` required | No argument help text is declared; parser destination is `source_header_id`. |
| `target_header_id` required | No argument help text is declared; parser destination is `target_header_id`. |
| `--reason` required | No argument help text is declared; parser destination is `reason`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp headers synthesize`

synthesize command

### Usage

```
x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id
```

### Syntax example

```
x86decomp headers synthesize example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `header_id` required | No argument help text is declared; parser destination is `header_id`. |
| `--output-root` | No argument help text is declared; parser destination is `output_root`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp headers validate`

validate command

### Usage

```
x86decomp headers validate [-h] header_id
```

### Syntax example

```
x86decomp headers validate example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `header_id` required | No argument help text is declared; parser destination is `header_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

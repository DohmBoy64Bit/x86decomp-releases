---
title: x86decomp provenance
description: Canonical provenance commands implemented by the current capability subsystem.
original_path: commands/provenance.html
---

<a id="command-provenance-binary"></a>
<a id="command-provenance-export"></a>
<a id="command-provenance-record"></a>
<a id="command-provenance-source"></a>

Section: Command reference

# `x86decomp provenance`

Canonical provenance commands implemented by the current capability subsystem.

Metadata: current · canonical group · 4 runnable paths

## Help

```
x86decomp provenance --help
```

Metadata: current · reconstruction

## `x86decomp provenance binary`

binary command

### Usage

```
x86decomp provenance binary [-h] [--address ADDRESS] binary_id
```

### Syntax example

```
x86decomp provenance binary target-exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `binary_id` required | No argument help text is declared; parser destination is `binary_id`. |
| `--address` | No argument help text is declared; parser destination is `address`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp provenance export`

export command

### Usage

```
x86decomp provenance export [-h] output
```

### Syntax example

```
x86decomp provenance export ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp provenance record`

record command

### Usage

```
x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON
                                   --confidence CONFIDENCE
                                   source_path line_start line_end binary_id
                                   address_start address_end
```

### Syntax example

```
x86decomp provenance record ./candidate.c 1 1 target-exe 0x401000 0x401000 --evidence-json ./evidence.json --confidence 1.0
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source_path` required | No argument help text is declared; parser destination is `source_path`. |
| `line_start` required · type: int | No argument help text is declared; parser destination is `line_start`. |
| `line_end` required · type: int | No argument help text is declared; parser destination is `line_end`. |
| `binary_id` required | No argument help text is declared; parser destination is `binary_id`. |
| `address_start` required | No argument help text is declared; parser destination is `address_start`. |
| `address_end` required | No argument help text is declared; parser destination is `address_end`. |
| `--evidence-json` required | No argument help text is declared; parser destination is `evidence_json`. |
| `--confidence` required · type: float | No argument help text is declared; parser destination is `confidence`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp provenance source`

source command

### Usage

```
x86decomp provenance source [-h] [--line LINE] source_path
```

### Syntax example

```
x86decomp provenance source ./candidate.c
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source_path` required | No argument help text is declared; parser destination is `source_path`. |
| `--line` type: int | No argument help text is declared; parser destination is `line`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

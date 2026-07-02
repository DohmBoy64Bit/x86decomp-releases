---
title: x86decomp boundary
description: Canonical boundary commands implemented by the current capability subsystem.
original_path: commands/boundary.html
---

<a id="command-boundary-audit"></a>
<a id="command-boundary-audit-project"></a>
<a id="command-boundary-export-ghidra-fixes"></a>
<a id="command-boundary-list"></a>
<a id="command-boundary-show"></a>

Section: Command reference

# `x86decomp boundary`

Canonical boundary commands implemented by the current capability subsystem.

Metadata: current · canonical group · 5 runnable paths

## Help

```
x86decomp boundary --help
```

Metadata: current · native

## `x86decomp boundary audit`

audit command

### Usage

```
x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA]
                                inventory_json
```

### Syntax example

```
x86decomp boundary audit ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `inventory_json` required | No argument help text is declared; parser destination is `inventory_json`. |
| `--text-end-rva` | No argument help text is declared; parser destination is `text_end_rva`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp boundary audit-project`

audit-project command

### Usage

```
x86decomp boundary audit-project [-h] artifact_project binary
```

### Syntax example

```
x86decomp boundary audit-project ./work ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `artifact_project` required | No argument help text is declared; parser destination is `artifact_project`. |
| `binary` required | No argument help text is declared; parser destination is `binary`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp boundary export-ghidra-fixes`

export-ghidra-fixes command

### Usage

```
x86decomp boundary export-ghidra-fixes [-h] output
```

### Syntax example

```
x86decomp boundary export-ghidra-fixes ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp boundary list`

list command

### Usage

```
x86decomp boundary list [-h] [--classification CLASSIFICATION]
```

### Syntax example

```
x86decomp boundary list
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--classification` | No argument help text is declared; parser destination is `classification`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp boundary show`

show command

### Usage

```
x86decomp boundary show [-h] function_id
```

### Syntax example

```
x86decomp boundary show pe-rva:00001000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `function_id` required | No argument help text is declared; parser destination is `function_id`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

---
title: x86decomp pe
description: Canonical pe commands implemented by the current capability subsystem.
original_path: commands/pe.html
---

<a id="command-pe-export-coff"></a>
<a id="command-pe-export-sections"></a>
<a id="command-pe-inventory"></a>
<a id="command-pe-patch-apply"></a>
<a id="command-pe-patch-plan"></a>
<a id="command-pe-text-swap"></a>

Section: Command reference

# `x86decomp pe`

Canonical pe commands implemented by the current capability subsystem.

Metadata: current · canonical group · 6 runnable paths

## Help

```
x86decomp pe --help
```

Metadata: current · native

## `x86decomp pe export-coff`

export-coff command

### Usage

```
x86decomp pe export-coff [-h] [--section SECTION] image output
```

### Syntax example

```
x86decomp pe export-coff ./target.exe ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `image` required | No argument help text is declared; parser destination is `image`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--section` | No argument help text is declared; parser destination is `section`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp pe export-sections`

export-sections command

### Usage

```
x86decomp pe export-sections [-h] [--section SECTION] image output
```

### Syntax example

```
x86decomp pe export-sections ./target.exe ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `image` required | No argument help text is declared; parser destination is `image`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--section` | No argument help text is declared; parser destination is `section`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp pe inventory`

inventory command

### Usage

```
x86decomp pe inventory [-h] image
```

### Syntax example

```
x86decomp pe inventory ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `image` required | No argument help text is declared; parser destination is `image`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp pe patch-apply`

patch-apply command

### Usage

```
x86decomp pe patch-apply [-h] plan_id
```

### Syntax example

```
x86decomp pe patch-apply example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `plan_id` required | No argument help text is declared; parser destination is `plan_id`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp pe patch-plan`

patch-plan command

### Usage

```
x86decomp pe patch-plan [-h] original output operations_json
```

### Syntax example

```
x86decomp pe patch-plan ./original.bin ./output.json ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `original` required | No argument help text is declared; parser destination is `original`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `operations_json` required | No argument help text is declared; parser destination is `operations_json`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp pe text-swap`

text-swap command

### Usage

```
x86decomp pe text-swap [-h] [--section-name SECTION_NAME]
                              original replacement output
```

### Syntax example

```
x86decomp pe text-swap ./original.bin example ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `original` required | No argument help text is declared; parser destination is `original`. |
| `replacement` required | No argument help text is declared; parser destination is `replacement`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--section-name` default: '.text' | No argument help text is declared; parser destination is `section_name`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

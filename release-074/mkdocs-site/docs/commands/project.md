---
title: x86decomp project
description: Canonical project commands implemented by the current capability subsystem.
original_path: commands/project.html
---

<a id="command-project-check"></a>
<a id="command-project-explain-boundaries"></a>
<a id="command-project-export"></a>
<a id="command-project-init"></a>
<a id="command-project-synthesize-layout"></a>

Section: Command reference

# `x86decomp project`

Canonical project commands implemented by the current capability subsystem.

Metadata: current · canonical group · 5 runnable paths

## Help

```
x86decomp project --help
```

Metadata: current · assembly

## `x86decomp project check`

check command

### Usage

```
x86decomp project check [-h]
```

### Syntax example

```
x86decomp project check
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp project explain-boundaries`

explain-boundaries command

### Usage

```
x86decomp project explain-boundaries [-h] module_id
```

### Syntax example

```
x86decomp project explain-boundaries example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `module_id` required | No argument help text is declared; parser destination is `module_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp project export`

export command

### Usage

```
x86decomp project export [-h] output
```

### Syntax example

```
x86decomp project export ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp project init`

init command

### Usage

```
x86decomp project init [-h]
```

### Syntax example

```
x86decomp project init
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp project synthesize-layout`

synthesize-layout command

### Usage

```
x86decomp project synthesize-layout [-h] inventory_json
```

### Syntax example

```
x86decomp project synthesize-layout ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `inventory_json` required | No argument help text is declared; parser destination is `inventory_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

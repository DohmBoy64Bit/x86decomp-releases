---
title: x86decomp runtime
description: Canonical runtime commands implemented by the current capability subsystem.
original_path: commands/runtime.html
---

<a id="command-runtime-launch"></a>
<a id="command-runtime-map-crash"></a>
<a id="command-runtime-validate-image"></a>

Section: Command reference

# `x86decomp runtime`

Canonical runtime commands implemented by the current capability subsystem.

Metadata: current · canonical group · 3 runnable paths

## Help

```
x86decomp runtime --help
```

Metadata: current · native

## `x86decomp runtime launch`

launch command

### Usage

```
x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT]
                                [--execute]
                                image
```

### Syntax example

```
x86decomp runtime launch ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `image` required | No argument help text is declared; parser destination is `image`. |
| `--argument` default: [] | No argument help text is declared; parser destination is `argument`. |
| `--timeout` default: 10 · type: int | No argument help text is declared; parser destination is `timeout`. |
| `--execute` nargs: 0 · default: False | No argument help text is declared; parser destination is `execute`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp runtime map-crash`

map-crash command

### Usage

```
x86decomp runtime map-crash [-h] rva
```

### Syntax example

```
x86decomp runtime map-crash 0x1000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `rva` required | No argument help text is declared; parser destination is `rva`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp runtime validate-image`

validate-image command

### Usage

```
x86decomp runtime validate-image [-h] image
```

### Syntax example

```
x86decomp runtime validate-image ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `image` required | No argument help text is declared; parser destination is `image`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

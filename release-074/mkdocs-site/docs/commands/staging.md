---
title: x86decomp staging
description: Canonical staging commands implemented by the current capability subsystem.
original_path: commands/staging.html
---

<a id="command-staging-compile-check"></a>
<a id="command-staging-generate-context"></a>
<a id="command-staging-resolve"></a>
<a id="command-staging-scan"></a>
<a id="command-staging-unresolved"></a>

Section: Command reference

# `x86decomp staging`

Canonical staging commands implemented by the current capability subsystem.

Metadata: current · canonical group · 5 runnable paths

## Help

```
x86decomp staging --help
```

Metadata: current · native

## `x86decomp staging compile-check`

compile-check command

### Usage

```
x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT]
                                       command_json
```

### Syntax example

```
x86decomp staging compile-check ./command.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `command_json` required | No argument help text is declared; parser destination is `command_json`. |
| `--cwd` | No argument help text is declared; parser destination is `cwd`. |
| `--timeout` default: 120 · type: int | No argument help text is declared; parser destination is `timeout`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp staging generate-context`

generate-context command

### Usage

```
x86decomp staging generate-context [-h] output sources [sources ...]
```

### Syntax example

```
x86decomp staging generate-context ./output.json ./candidate.c
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `sources` required · nargs: + | No argument help text is declared; parser destination is `sources`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp staging resolve`

resolve command

### Usage

```
x86decomp staging resolve [-h] mapping_json
```

### Syntax example

```
x86decomp staging resolve ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `mapping_json` required | No argument help text is declared; parser destination is `mapping_json`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp staging scan`

scan command

### Usage

```
x86decomp staging scan [-h] sources [sources ...]
```

### Syntax example

```
x86decomp staging scan ./candidate.c
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `sources` required · nargs: + | No argument help text is declared; parser destination is `sources`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp staging unresolved`

unresolved command

### Usage

```
x86decomp staging unresolved [-h]
```

### Syntax example

```
x86decomp staging unresolved
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

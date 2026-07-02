---
title: x86decomp windows
description: Canonical windows commands implemented by the current capability subsystem.
original_path: commands/windows.html
---

<a id="command-windows-discover-ghidra"></a>
<a id="command-windows-doctor"></a>
<a id="command-windows-response-file"></a>

Section: Command reference

# `x86decomp windows`

Canonical windows commands implemented by the current capability subsystem.

Metadata: current · canonical group · 3 runnable paths

## Help

```
x86decomp windows --help
```

Metadata: current · native

## `x86decomp windows discover-ghidra`

discover-ghidra command

### Usage

```
x86decomp windows discover-ghidra [-h] [--ghidra-home GHIDRA_HOME]
                                         [--platform-name PLATFORM_NAME]
```

### Syntax example

```
x86decomp windows discover-ghidra
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--ghidra-home` | No argument help text is declared; parser destination is `ghidra_home`. |
| `--platform-name` | No argument help text is declared; parser destination is `platform_name`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp windows doctor`

doctor command

### Usage

```
x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]
```

### Syntax example

```
x86decomp windows doctor
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--ghidra-home` | No argument help text is declared; parser destination is `ghidra_home`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp windows response-file`

response-file command

### Usage

```
x86decomp windows response-file [-h] output arguments_json
```

### Syntax example

```
x86decomp windows response-file ./output.json {}
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `arguments_json` required | No argument help text is declared; parser destination is `arguments_json`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

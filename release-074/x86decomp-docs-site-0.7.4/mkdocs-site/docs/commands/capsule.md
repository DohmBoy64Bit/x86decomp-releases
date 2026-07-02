---
title: x86decomp capsule
description: Canonical capsule commands implemented by the current capability subsystem.
original_path: commands/capsule.html
---

<a id="command-capsule-create"></a>
<a id="command-capsule-inspect"></a>
<a id="command-capsule-reproduce"></a>
<a id="command-capsule-verify"></a>

Section: Command reference

# `x86decomp capsule`

Canonical capsule commands implemented by the current capability subsystem.

Metadata: current · canonical group · 4 runnable paths

## Help

```
x86decomp capsule --help
```

Metadata: current · reconstruction

## `x86decomp capsule create`

create command

### Usage

```
x86decomp capsule create [-h] [--include INCLUDE]
                                [--external-json EXTERNAL_JSON]
                                name output
```

### Syntax example

```
x86decomp capsule create example ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--include` default: [] | No argument help text is declared; parser destination is `include`. |
| `--external-json` | No argument help text is declared; parser destination is `external_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp capsule inspect`

inspect command

### Usage

```
x86decomp capsule inspect [-h] path
```

### Syntax example

```
x86decomp capsule inspect ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp capsule reproduce`

reproduce command

### Usage

```
x86decomp capsule reproduce [-h] path destination
```

### Syntax example

```
x86decomp capsule reproduce ./input.json example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |
| `destination` required | No argument help text is declared; parser destination is `destination`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp capsule verify`

verify command

### Usage

```
x86decomp capsule verify [-h] path
```

### Syntax example

```
x86decomp capsule verify ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

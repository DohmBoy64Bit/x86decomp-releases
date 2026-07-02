---
title: x86decomp hybrid
description: Canonical hybrid commands implemented by the current capability subsystem.
original_path: commands/hybrid.html
---

<a id="command-hybrid-compose"></a>
<a id="command-hybrid-generate"></a>
<a id="command-hybrid-verify"></a>

Section: Command reference

# `x86decomp hybrid`

Canonical hybrid commands implemented by the current capability subsystem.

Metadata: current · canonical group · 3 runnable paths

## Help

```
x86decomp hybrid --help
```

Metadata: current · native

## `x86decomp hybrid compose`

compose command

### Usage

```
x86decomp hybrid compose [-h] run_id output
```

### Syntax example

```
x86decomp hybrid compose example-001 ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `run_id` required | No argument help text is declared; parser destination is `run_id`. |
| `output` required | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · assembly

## `x86decomp hybrid generate`

generate command

### Usage

```
x86decomp hybrid generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 source_project output
```

### Syntax example

```
x86decomp hybrid generate ./work ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source_project` required | No argument help text is declared; parser destination is `source_project`. |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |
| `--asm-format` default: 'bytes' · choices: bytes, annotated, mnemonic | No argument help text is declared; parser destination is `asm_format`. |
| `--image-base` default: 0 · type: _int | No argument help text is declared; parser destination is `image_base`. |
| `--assembler-command-json` | No argument help text is declared; parser destination is `assembler_command_json`. |
| `--symbol-map` | No argument help text is declared; parser destination is `symbol_map`. |
| `--overwrite` nargs: 0 · default: False | No argument help text is declared; parser destination is `overwrite`. |

> **Source basis.** Parser definition: `src/x86decomp/assembly/cli.py`; SHA-256 `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp hybrid verify`

verify command

### Usage

```
x86decomp hybrid verify [-h] composition_id
```

### Syntax example

```
x86decomp hybrid verify example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `composition_id` required | No argument help text is declared; parser destination is `composition_id`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

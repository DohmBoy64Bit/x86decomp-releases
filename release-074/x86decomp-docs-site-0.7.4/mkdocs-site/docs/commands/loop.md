---
title: x86decomp loop
description: Canonical loop commands implemented by the current capability subsystem.
original_path: commands/loop.html
---

<a id="command-loop-list"></a>
<a id="command-loop-run"></a>
<a id="command-loop-show"></a>

Section: Command reference

# `x86decomp loop`

Canonical loop commands implemented by the current capability subsystem.

Metadata: current · canonical group · 3 runnable paths

## Help

```
x86decomp loop --help
```

Metadata: current · native

## `x86decomp loop list`

list command

### Usage

```
x86decomp loop list [-h]
```

### Syntax example

```
x86decomp loop list
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp loop run`

run command

### Usage

```
x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY]
                          [--timeout TIMEOUT] [--execute]
                          function_id source compile_command_json candidate
                          original rva slot_size
```

### Syntax example

```
x86decomp loop run pe-rva:00001000 ./candidate.c ./compile-command.json ./candidate.bin ./original.bin 0x1000 1
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `function_id` required | No argument help text is declared; parser destination is `function_id`. |
| `source` required | No argument help text is declared; parser destination is `source`. |
| `compile_command_json` required | No argument help text is declared; parser destination is `compile_command_json`. |
| `candidate` required | No argument help text is declared; parser destination is `candidate`. |
| `original` required | No argument help text is declared; parser destination is `original`. |
| `rva` required | No argument help text is declared; parser destination is `rva`. |
| `slot_size` required · type: int | No argument help text is declared; parser destination is `slot_size`. |
| `--symbol` | No argument help text is declared; parser destination is `symbol`. |
| `--policy` default: 'trailing-padding' | No argument help text is declared; parser destination is `policy`. |
| `--timeout` default: 120 · type: int | No argument help text is declared; parser destination is `timeout`. |
| `--execute` nargs: 0 · default: False | No argument help text is declared; parser destination is `execute`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp loop show`

show command

### Usage

```
x86decomp loop show [-h] loop_id
```

### Syntax example

```
x86decomp loop show example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `loop_id` required | No argument help text is declared; parser destination is `loop_id`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

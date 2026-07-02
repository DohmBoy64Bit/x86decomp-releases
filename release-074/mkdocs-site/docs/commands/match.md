---
title: x86decomp match
description: Canonical match commands implemented by the current capability subsystem.
original_path: commands/match.html
---

<a id="command-match-batch"></a>
<a id="command-match-compare"></a>
<a id="command-match-mismatches"></a>
<a id="command-match-report"></a>

Section: Command reference

# `x86decomp match`

Canonical match commands implemented by the current capability subsystem.

Metadata: current · canonical group · 4 runnable paths

## Help

```
x86decomp match --help
```

Metadata: current · native

## `x86decomp match batch`

batch command

### Usage

```
x86decomp match batch [-h] [--policy {exact,trailing-padding}]
                             [--pad-bytes-json PAD_BYTES_JSON]
                             original candidates_json
```

### Syntax example

```
x86decomp match batch ./original.bin ./candidate.bin
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `original` required | No argument help text is declared; parser destination is `original`. |
| `candidates_json` required | No argument help text is declared; parser destination is `candidates_json`. |
| `--policy` default: 'trailing-padding' · choices: exact, trailing-padding | No argument help text is declared; parser destination is `policy`. |
| `--pad-bytes-json` | No argument help text is declared; parser destination is `pad_bytes_json`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp match compare`

compare command

### Usage

```
x86decomp match compare [-h] [--policy {exact,trailing-padding}]
                               [--pad-bytes-json PAD_BYTES_JSON]
                               [--protected-offsets-json PROTECTED_OFFSETS_JSON]
                               original candidate
```

### Syntax example

```
x86decomp match compare ./original.bin ./candidate.bin
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `original` required | No argument help text is declared; parser destination is `original`. |
| `candidate` required | No argument help text is declared; parser destination is `candidate`. |
| `--policy` default: 'trailing-padding' · choices: exact, trailing-padding | No argument help text is declared; parser destination is `policy`. |
| `--pad-bytes-json` | No argument help text is declared; parser destination is `pad_bytes_json`. |
| `--protected-offsets-json` | No argument help text is declared; parser destination is `protected_offsets_json`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp match mismatches`

mismatches command

### Usage

```
x86decomp match mismatches [-h] run_id
```

### Syntax example

```
x86decomp match mismatches example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `run_id` required | No argument help text is declared; parser destination is `run_id`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · native

## `x86decomp match report`

report command

### Usage

```
x86decomp match report [-h] run_id
```

### Syntax example

```
x86decomp match report example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `run_id` required | No argument help text is declared; parser destination is `run_id`. |

> **Source basis.** Parser definition: `src/x86decomp/native/cli.py`; SHA-256 `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950`. Descriptions above use only parser-declared text or an explicit no-help notice.

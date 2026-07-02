---
title: x86decomp hypothesis
description: Canonical hypothesis commands implemented by the current capability subsystem.
original_path: commands/hypothesis.html
---

<a id="command-hypothesis-create"></a>
<a id="command-hypothesis-dependency"></a>
<a id="command-hypothesis-evidence"></a>
<a id="command-hypothesis-gate"></a>
<a id="command-hypothesis-list"></a>
<a id="command-hypothesis-show"></a>
<a id="command-hypothesis-transition"></a>

Section: Command reference

# `x86decomp hypothesis`

Canonical hypothesis commands implemented by the current capability subsystem.

Metadata: current · canonical group · 7 runnable paths

## Help

```
x86decomp hypothesis --help
```

Metadata: current · governance

## `x86decomp hypothesis create`

create command

### Usage

```
x86decomp hypothesis create [-h] --origin ORIGIN
                                   statement scope_kind scope_id
```

### Syntax example

```
x86decomp hypothesis create recovered-parser-loop function pe-rva:00001000 --origin analyst
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `statement` required | No argument help text is declared; parser destination is `statement`. |
| `scope_kind` required | No argument help text is declared; parser destination is `scope_kind`. |
| `scope_id` required | No argument help text is declared; parser destination is `scope_id`. |
| `--origin` required | No argument help text is declared; parser destination is `origin`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp hypothesis dependency`

dependency command

### Usage

```
x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id
```

### Syntax example

```
x86decomp hypothesis dependency hypothesis-001 ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `hypothesis_id` required | No argument help text is declared; parser destination is `hypothesis_id`. |
| `depends_on_id` required | No argument help text is declared; parser destination is `depends_on_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp hypothesis evidence`

evidence command

### Usage

```
x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT
                                     --kind KIND --group GROUP
                                     [--artifact-sha256 ARTIFACT_SHA256]
                                     [--details-json DETAILS_JSON]
                                     hypothesis_id evidence_id
```

### Syntax example

```
x86decomp hypothesis evidence hypothesis-001 example-001 --stance support --weight 1.0 --kind analysis --group independent-source
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `hypothesis_id` required | No argument help text is declared; parser destination is `hypothesis_id`. |
| `evidence_id` required | No argument help text is declared; parser destination is `evidence_id`. |
| `--stance` required | No argument help text is declared; parser destination is `stance`. |
| `--weight` required · type: float | No argument help text is declared; parser destination is `weight`. |
| `--kind` required | No argument help text is declared; parser destination is `kind`. |
| `--group` required · default: 'hypothesis' | No argument help text is declared; parser destination is `group`. |
| `--artifact-sha256` | No argument help text is declared; parser destination is `artifact_sha256`. |
| `--details-json` | No argument help text is declared; parser destination is `details_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp hypothesis gate`

gate command

### Usage

```
x86decomp hypothesis gate [-h] hypothesis_id
```

### Syntax example

```
x86decomp hypothesis gate hypothesis-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `hypothesis_id` required | No argument help text is declared; parser destination is `hypothesis_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp hypothesis list`

list command

### Usage

```
x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]
```

### Syntax example

```
x86decomp hypothesis list
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--state` | No argument help text is declared; parser destination is `state`. |
| `--scope-id` | No argument help text is declared; parser destination is `scope_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp hypothesis show`

show command

### Usage

```
x86decomp hypothesis show [-h] hypothesis_id
```

### Syntax example

```
x86decomp hypothesis show hypothesis-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `hypothesis_id` required | No argument help text is declared; parser destination is `hypothesis_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp hypothesis transition`

transition command

### Usage

```
x86decomp hypothesis transition [-h] --reason REASON [--lock]
                                       hypothesis_id state
```

### Syntax example

```
x86decomp hypothesis transition hypothesis-001 active --reason reviewed-change
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `hypothesis_id` required | No argument help text is declared; parser destination is `hypothesis_id`. |
| `state` required | No argument help text is declared; parser destination is `state`. |
| `--reason` required | No argument help text is declared; parser destination is `reason`. |
| `--lock` nargs: 0 · default: False | No argument help text is declared; parser destination is `lock`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

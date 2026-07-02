---
title: x86decomp consensus
description: Canonical consensus commands implemented by the current capability subsystem.
original_path: commands/consensus.html
---

<a id="command-consensus-conflicts"></a>
<a id="command-consensus-explain"></a>
<a id="command-consensus-record"></a>
<a id="command-consensus-resolve"></a>
<a id="command-consensus-scan"></a>

Section: Command reference

# `x86decomp consensus`

Canonical consensus commands implemented by the current capability subsystem.

Metadata: current · canonical group · 5 runnable paths

## Help

```
x86decomp consensus --help
```

Metadata: current · governance

## `x86decomp consensus conflicts`

conflicts command

### Usage

```
x86decomp consensus conflicts [-h]
```

### Syntax example

```
x86decomp consensus conflicts
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp consensus explain`

explain command

### Usage

```
x86decomp consensus explain [-h] subject_kind subject_id property_name
```

### Syntax example

```
x86decomp consensus explain analysis example-001 ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `subject_kind` required | No argument help text is declared; parser destination is `subject_kind`. |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |
| `property_name` required | No argument help text is declared; parser destination is `property_name`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp consensus record`

record command

### Usage

```
x86decomp consensus record [-h] --adapter ADAPTER
                                  --adapter-version ADAPTER_VERSION
                                  --evidence-id EVIDENCE_ID --group GROUP
                                  [--confidence CONFIDENCE]
                                  subject_kind subject_id property_name
                                  value_json
```

### Syntax example

```
x86decomp consensus record analysis example-001 ./target.exe ./output.json --adapter capstone --adapter-version 1.0 --evidence-id example-001 --group independent-source
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `subject_kind` required | No argument help text is declared; parser destination is `subject_kind`. |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |
| `property_name` required | No argument help text is declared; parser destination is `property_name`. |
| `value_json` required | No argument help text is declared; parser destination is `value_json`. |
| `--adapter` required | No argument help text is declared; parser destination is `adapter`. |
| `--adapter-version` required | No argument help text is declared; parser destination is `adapter_version`. |
| `--evidence-id` required | No argument help text is declared; parser destination is `evidence_id`. |
| `--group` required · default: 'consensus' | No argument help text is declared; parser destination is `group`. |
| `--confidence` default: 1.0 · type: float | No argument help text is declared; parser destination is `confidence`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp consensus resolve`

resolve command

### Usage

```
x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE
                                   [--lock]
                                   subject_kind subject_id property_name
                                   selected_value_json
```

### Syntax example

```
x86decomp consensus resolve analysis example-001 ./target.exe ./output.json --method evidence-weighted --rationale reviewed-change
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `subject_kind` required | No argument help text is declared; parser destination is `subject_kind`. |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |
| `property_name` required | No argument help text is declared; parser destination is `property_name`. |
| `selected_value_json` required | No argument help text is declared; parser destination is `selected_value_json`. |
| `--method` required | No argument help text is declared; parser destination is `method`. |
| `--rationale` required | No argument help text is declared; parser destination is `rationale`. |
| `--lock` nargs: 0 · default: False | No argument help text is declared; parser destination is `lock`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp consensus scan`

scan command

### Usage

```
x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND]
                                [--subject-id SUBJECT_ID]
```

### Syntax example

```
x86decomp consensus scan
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--subject-kind` | No argument help text is declared; parser destination is `subject_kind`. |
| `--subject-id` | No argument help text is declared; parser destination is `subject_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
